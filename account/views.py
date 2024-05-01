from datetime import datetime
from json import JSONDecodeError

import jwt,datetime
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from account.models import Profile
from account.serializers import ProfileSerializer, UserSerializer, LoginSerializer
from rest_framework.authtoken.models import Token


# Create your views here.
class ProfileList(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    def get(self, request):
        token = request.COOKIES.get('token')
        if not token:
           return AuthenticationFailed('Token is missing')
        try:
             payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except:
             return AuthenticationFailed('Token is missing')
        try:
            user = Profile.objects.get(pk=payload['id'])
        except Profile.DoesNotExist:
            return Response("Profile does not exist")
        serializer = ProfileSerializer(user)
        return Response(serializer.data)



    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = ProfileSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error", "message": "Invalid JSON"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = ProfileSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError as e:
            return JsonResponse({"result": "error", "message": "Invalid JSON"}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        data = JSONParser().parse(request)
        obj = Profile.objects.get(id=data['id'])
        serializer = ProfileSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        data = JSONParser().parse(request)
        obj = Profile.objects.get(id=data['id'])
        obj.delete()
        return Response({"message": "person deleted"})

    def get_username(self, obj):
        username_obj = Profile.user.get_username()
        return {'username': username_obj}

    def search(self, request):
        search = request.GET.get('search')
        queryset = self.queryset
        if search is not None:
            queryset = queryset.filter(user__first_name__startswith=search)
            serializer = ProfileSerializer(queryset, many=True)
            return Response({"status": 200, "data": serializer.data})


class ProfileListUpDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "pk"


class loginAPI(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def get(self, request):
        serializer = LoginSerializer(User.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if not user:
            return Response({
                "status": False,
                "message": "invalid user"
            }, status.HTTP_400_BAD_REQUEST)
        payload={
            'id':user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token=jwt.encode(payload,'secret',algorithm='HS256')
        response=Response()
        response.set_cookie(key='token',value=token,httponly=True)
        response.data={
            'token': str(token)
        }
        return response



class RegisterAPI(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                "status": False,
                "message": "invalid data"
            }, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'status': True, "message": "user created", "data": serializer.data}, status.HTTP_201_CREATED)

class LogoutAPI(generics.GenericAPIView):
    def post(self, request):
        response=Response()
        response.delete_cookie(key='token')
        response.data={
            'message': 'logged out'
        }
        return response