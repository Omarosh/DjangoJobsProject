from django.shortcuts import render
from django.http import JsonResponse

from account.api.v1.serializers import UserSerializer
from job.models import Job
from .serializers import JobSerializer, CreateSerializer
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from job.decorators import IsDeveloper,IsCompany, IsNotApplied, IsNotWorking
from account.models import User

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsCompany])
def create_job(request,format=None):
    data = request.data
    uid = User.objects.get(username=request.user).id
    data["created_by"] = uid
    serializer = CreateSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        print('data ==>',serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"Hi" : "Hi"})

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsCompany])
def accept_developer_for_job(request, id, format=None):
    # user = User.objects.get(username=request.user)
    user = User.objects.get(username=request.data['username'])
    job = Job.objects.get(pk=id)
    print("Before")
    print(job.developer)
    job.developer = user
    job.status = "Inprogress"
    job.applied_developers= []
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


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsDeveloper, IsNotApplied, IsNotWorking])
def job_apply(request, id, format=None):
    user = User.objects.get(username=request.user)
    job = Job.objects.get(pk=id)
    job.applied_developers.add(user)

    serializer = JobSerializer(job)
    return Response(serializer.data)

    # return JsonResponse({"jobs": "Testing"})

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_applied_developers_job(request, id, format=None):
    job = Job.objects.get(pk=id)
    serializer = UserSerializer(job.applied_developers, many=True)
    return Response(serializer.data)
    # return JsonResponse({"jobs": serializer.data})

    # return JsonResponse({"jobs": "Testing"})

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def finish_job(request,id,format=None):
    try:
        job = Job.objects.get(pk=id)
        user = User.objects.get(username=request.user)
        if user.id  == job.developer.id or user.id == job.created_by.id:
            if job.status == 'Inprogress':
                job.status ='Finished'
                job.save()
                return JsonResponse({"Success": "Job status changed to Finished!"})
            else:
                return JsonResponse({"Failed": "Job status is not in progress"})
        else:
            return JsonResponse({"Failed": "yor not Authorized to finish this job"})

    except Job.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)






