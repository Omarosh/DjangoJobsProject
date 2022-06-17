from rest_framework.permissions import BasePermission
from account.models import User
from .models import Job
from account.api.v1.serializers import UserSerializer

class IsCompany(BasePermission):
    def has_permission(self, request, view):
        user = User.objects.filter(username=request.user)
        return user.filter(user_type="c").exists()

class IsDeveloper(BasePermission):
    def has_permission(self, request, view):
        user = User.objects.filter(username=request.user)
        return user.filter(user_type="d").exists()


class IsNotApplied(BasePermission):
    def has_permission(self, request, view):
        user = User.objects.get(username=request.user)
        jobs = Job.objects.all()
        print("Hi")
        for job in jobs:
            for dev in job.applied_developers.values():
                if user.id == dev['id']:
                    return False
            # serilaizer = UserSerializer(job.applied_developers)
            # after = ss.contains(user.id)
            # print(after)

        return True
        # return user.filter(user_type="d").exists()