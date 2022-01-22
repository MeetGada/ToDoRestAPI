from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}
    
    # manually defining create() to save the hashed password
    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class workSerializer(serializers.ModelSerializer):
    class Meta:
        model = work
        fields = '__all__'
    # since, owner of the task should not be changed so, defining user to read_only 
        extra_kwargs = {'user': {'read_only': True}}
