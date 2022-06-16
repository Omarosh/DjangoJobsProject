from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, CompanySerializer
from django.contrib.auth import get_user_model
from django.contrib.auth import logout
from django.contrib import messages
from account.models import User
from django.http import JsonResponse

User = get_user_model()


#
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
@api_view(['POST'])
@permission_classes([])
def signupUser(request):
    response = {'data': None, 'status': status.HTTP_400_BAD_REQUEST}
    print(request.data)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response['data'] = serializer.data
        response['status'] = status.HTTP_201_CREATED
    else:
        response['data'] = serializer.errors

    return Response(**response)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
@permission_classes([])
def signupCompany(request):
    response = {'data': None, 'status': status.HTTP_400_BAD_REQUEST}
    print(request.data)
    serializer = CompanySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response['data'] = serializer.data
        response['status'] = status.HTTP_201_CREATED
    else:
        response['data'] = serializer.errors

    return Response(**response)


@api_view(['GET'])
@permission_classes([])
def list_user(request):
    user_objects = User.objects.filter(user_type='d')
    serializer = UserSerializer(user_objects, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([])
def list_company(request):
    company_object = User.objects.filter(user_type='c')
    serializer = CompanySerializer(company_object, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([])
def user_details(request, user_id):
    user_object = User.objects.filter(user_type='d').get(pk=user_id)
    serializer = UserSerializer(user_object)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([])
def company_details(request, company_id):
    company_object = User.objects.filter(user_type='c').get(pk=company_id)
    serializer = CompanySerializer(company_object)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([])
def List(request, user_type):
    if user_type == 'd':
        list_object = User.objects.filter(user_type='d')
        serializer = UserSerializer(list_object, many=True)
    else:
        list_object = User.objects.filter(user_type='c')
        serializer = CompanySerializer(list_object, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([])
def details(request, user_type, ids):
    details_object = User.objects.filter(user_type=user_type).get(pk=ids)
    if user_type == 'c':
        serializer = CompanySerializer(details_object)
    else:
        serializer = UserSerializer(details_object)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT', 'PATCH'])
@permission_classes([])
def update(request, user_type, ids):
    response = {'data': None, 'status': status.HTTP_400_BAD_REQUEST}

    update_instance = User.objects.filter(user_type=user_type).get(pk=ids)

    if request.method == 'PUT':
        serializer = CompanySerializer(instance=update_instance, data=request.data)
    else:
        serializer = CompanySerializer(instance=update_instance, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        response['data'] = serializer.data
        response['status'] = status.HTTP_201_CREATED
    else:
        response['data'] = serializer.errors

    return Response(**response)


@api_view(['DELETE'])
@permission_classes([])
def delete(request, user_type, ids):
    User.objects.filter(user_type=user_type).get(pk=ids).delete()

    return Response(data={'detail': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout_user(request):
    # User.objects.get(username=request.user)
    print(request.user)
    request.user.auth_token.delete()
    logout(request)
    messages.success(request, ("You were logged out!"))
    return JsonResponse({"status": "logout"})
