from django.shortcuts import render
from rest_framework import generics
from account.models import Profile
from account.serializers import ProfileSerializer
# Create your views here.
class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer