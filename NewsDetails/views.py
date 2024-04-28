from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from NewsDetails.models import Magazine, Topic, MyNew
from NewsDetails.serializers import MagazineSerializer, TopicSerializer, MyNewSerializer


# Create your views here.
class MagazineList(generics.ListCreateAPIView):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = MagazineSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response("saved successfully", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        data = JSONParser().parse(request)
        obj = Magazine.objects.get(id=data['id'])
        obj.delete()
        return Response({"message": "person deleted"})



class MagazineUporDe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer
    lookup_field = 'pk'


class TopicList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def delete(self, request):
        data = JSONParser().parse(request)
        obj = Topic.objects.get(id=data['id'])
        obj.delete()
        return Response({"message": "person deleted"})


class TopicUPorDe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    lookup_field = 'pk'


class MyNewList(generics.ListCreateAPIView):
    queryset = MyNew.objects.all()
    serializer_class = MyNewSerializer

    def delete(self, request):
        data = JSONParser().parse(request)
        obj = MyNew.objects.get(id=data['id'])
        obj.delete()
        return Response({"message": "person deleted"})


class MyNewUporDe(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyNew.objects.all()
    serializer_class = MyNewSerializer
    lookup_field = 'pk'
