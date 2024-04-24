from django.contrib.auth.models import User
from rest_framework import serializers
from account.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("Username already exists")
        if User.objects.filter(password=data['password']).exists():
            raise serializers.ValidationError("Password already exists")
        return data

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


    def validate(self, data):
        if len(data['phone_number']) != 11:
            raise serializers.ValidationError('unvalidated phone number')
        try:
            int(data['phone_number'])
        except ValueError:
            raise serializers.ValidationError('unvalidated phone number')
        if data['phone_number']:
            if Profile.objects.filter(phone_number=data['phone_number']).exists():
                raise serializers.ValidationError('this phonenumber already exists')
        return data
