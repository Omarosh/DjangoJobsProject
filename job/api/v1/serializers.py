from rest_framework import serializers
from job.models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'name', 'description', 'tags', 'applied_developers']
        depth = 1


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
