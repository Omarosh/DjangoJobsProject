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

        ddd = Job.objects.all()
        for job in ddd:
            ss = job.applied_developers
            after  =  ss.exclude(pk=user.id)
            print(after)
        print(ddd)
        return True
        # return user.filter(user_type="d").exists()