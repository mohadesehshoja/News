from django.shortcuts import render
from rest_framework import generics
from NewsDetails.models import Magazine,Topic,MyNew
from NewsDetails.serializers import MagazineSerializer,TopicSerializer,MyNewSerializer
# Create your views here.
class MagazineList(generics.ListCreateAPIView):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer
class TopicList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class MyNewList(generics.ListCreateAPIView):
    queryset = MyNew.objects.all()
    serializer_class = MyNewSerializer


