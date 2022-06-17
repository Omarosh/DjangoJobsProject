from rest_framework import serializers
from job.models import Job
from account.api.v1.serializers import CustomUserSerializer


class JobSerializer(serializers.ModelSerializer):
    applied_developers = CustomUserSerializer(many=True)

    class Meta:

        fields = ['id', 'name', 'description', 'tags', 'applied_developers']
        # fields = '__all__'
        model = Job
        depth = 1


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
