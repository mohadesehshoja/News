from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from NewsDetails.models import Magazine,Topic,MyNew
from NewsDetails.serializers import MagazineSerializer,TopicSerializer,MyNewSerializer
# Create your views here.
class MagazineList(generics.ListCreateAPIView):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer
    def deleteall(self,request,*args,**kwargs):
        Magazine.objects.all().delete()
        return Response(status=status.HTTp_204_NO_CONTENT)

class MagazineUporDe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer
    lookup_field = 'pk'
class TopicList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    def deleteall(self,request,*args,**kwargs):
        Topic.objects.all().delete()
        return Response(status=status.HTTp_204_NO_CONTENT)

class TopicUPorDe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    lookup_field = 'pk'

class MyNewList(generics.ListCreateAPIView):
    queryset = MyNew.objects.all()
    serializer_class = MyNewSerializer
    def deleteall(self,request,*args,**kwargs):
        MyNew.objects.all().delete()
        return Response(status=status.HTTp_204_NO_CONTENT)

class MyNewUporDe(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyNew.objects.all()
    serializer_class = MyNewSerializer
    lookup_field = 'pk'



