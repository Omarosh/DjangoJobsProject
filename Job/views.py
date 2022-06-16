from django.shortcuts import render
from django.http import JsonResponse
from .models import Job
from .serializers import JobSerializer, CreateSerializer
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from .decorators import IsDeveloper,IsCompany, IsApplied
from account.models import User

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsCompany])
def create_job(request,format=None):
    print(request.data)
    serializer = CreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print('data ==>',serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsDeveloper])
def accept_developer_for_job(request, id, format=None):
    user = User.objects.get(username=request.user)
    job = Job.objects.get(pk=id)
    print("Before")
    print(job.developer)
    job.developer = user
    job.status = "Inprogress"
    job.save()
    job = Job.objects.get(pk=id)
    print("after")
    print(job.developer)
    return JsonResponse({"jobs": "hi"})

@api_view(['GET'])
def job_list(request,format=None):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return JsonResponse({"jobs": serializer.data})



@api_view(['GET', 'PUT', 'DELETE'])
def job_detail(request, id,format=None):
    print("Hiii: " + request.method)
    try:
        job = Job.objects.get(pk=id)
    except Job.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        print("Helloo")
        serializer = JobSerializer(job)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = JobSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        print(job.developer)
        if job.status == 'Open' and job.developer != "None":
            job.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsDeveloper, IsApplied])
def job_apply(request, id, format=None):
    # user = User.objects.get(username=request.user)
    # job = Job.objects.get(pk=id)
    # # print(job.applied_developers.update())
    # job.applied_developers.add(user)
    # serializer = JobSerializer(job, data=job)
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data)
    # return JsonResponse({"jobs": serializer.data})

    return JsonResponse({"jobs": "Testing"})