from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from account.models import Profile
from account.serializers import ProfileSerializer
# Create your views here.
class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    def deleteall(self,request,*args,**kwargs):
        Profile.objects.all().delete()
        return Response(status=status.HTTp_204_NO_CONTENT)


class ProfileListUpDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "pk"