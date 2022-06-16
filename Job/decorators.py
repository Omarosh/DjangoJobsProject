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

        print(12333333 + user.id)
        # ddd = Job.objects.filter(applied_developers__icontains=[user.id])
        ddd = Job.applied_developers.filter(pk=user.id)
        print(ddd)
        return True
        # return user.filter(user_type="d").exists()