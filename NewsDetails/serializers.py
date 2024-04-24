from rest_framework import serializers
from NewsDetails.models import Magazine,Topic,MyNew
class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class MyNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyNew
        fields = '__all__'
        depth:3

