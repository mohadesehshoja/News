from rest_framework import serializers
from NewsDetails.models import Magazine,Topic,MyNew
class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = '__all__'

    def validate(self, data):
        if data['phone_number'] is not None:
            if len(data['phone_number']) != 11:
                raise serializers.ValidationError('unvalidated phone number')
            try:
                int(data['phone_number'])
            except ValueError:
                raise serializers.ValidationError('unvalidated phone number')
            if data['phone_number']:
                if Magazine.objects.filter(phone_number=data['phone_number']).exists():
                    raise serializers.ValidationError('this phonenumber already exists')
        return data


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class MyNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyNew
        fields = '__all__'
        depth:3

