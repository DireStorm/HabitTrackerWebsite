from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

from .models import Profile


# from rest_framework.serializers import ModelSerializer
# from .models import Habit

#Habits Serializer
# class HabitSerializer(ModelSerializer):
#     class Meta:
#         model = Habit
#         fields = '__all__'

# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'password', 'email', 'first_name', 'last_name') # If you want to add more fields for registration, you need to update this and the validated data values
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],     password = validated_data['password'], email = validated_data['email'],     first_name=validated_data['first_name'],  last_name=validated_data['last_name'])
        return user

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'score']