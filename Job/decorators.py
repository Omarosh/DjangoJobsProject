from rest_framework.permissions import BasePermission
from account.models import User
from .models import Job

class IsCompany(BasePermission):
    def has_permission(self, request, view):
        user = User.objects.filter(username=request.user)
        return user.filter(user_type="c").exists()

class IsDeveloper(BasePermission):
    def has_permission(self, request, view):
        user = User.objects.filter(username=request.user)
        return user.filter(user_type="d").exists()


class IsApplied(BasePermission):
    def has_permission(self, request, view):
        user = User.objects.get(username=request.user)
        jobs = Job.objects.all()

        # print( user.id)
        # ddd = Job.objects.filter(applied_developers__icontains=[user.id])
        # ddd = Job.objects.all()
        # print(ddd)
        return True
        # return user.filter(user_type="d").exists()