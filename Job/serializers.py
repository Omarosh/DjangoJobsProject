from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['name','description','Tags','id']
        depth = 1


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
