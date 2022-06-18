from ctypes.wintypes import tagSIZE
from dataclasses import field
from rest_framework import serializers
from django.contrib.auth import get_user_model

import tag.models
from account.models import Notification
from tag.api.v1.serializers import TagSerializer
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)
    # tags = TagSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'password_confirm', 'email', 'user_type', 'gender', 'date_of_birth',
                  'tags']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
            # 'address': {'required': True},
            'gender': {'required': True},
            'tags':{'required': True}
        }
    def create(self, validated_data):
        if self.validated_data.get('password') != self.validated_data.get('password_confirm'):
            raise serializers.ValidationError('Password confirmation does not match')

        validated_data.pop('password')
        validated_data.pop('password_confirm')
        if 'tags' in validated_data:
            tags = validated_data.pop('tags')
        user = User(**validated_data)
        user.set_password(self.validated_data.get('password'))

        user.save()
        if 'tags' in locals():
            user.tags.set(tags)
        return user


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'tags']

class UpdateUserSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = User
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'password_confirm', 'email', 'user_type', 'gender']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
            'address': {'required': True},
            'history': {'required': True},

        }

    def save(self, **kwargs):
        print(self.validated_data['username'])
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            user_type=self.validated_data['user_type'],
            # address
            # history
        )

        if (self.validated_data['password'] != self.validated_data['password_confirm']):
            raise serializers.ValidationError({'details': 'passwords didnt match'})

        user.set_password(self.validated_data['password'])
        user.save()
        return user


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['message', 'creation_time']
