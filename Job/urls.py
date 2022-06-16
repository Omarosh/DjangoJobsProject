from django.contrib import admin
from django.urls import path
from .views import job_list,create_job,job_detail, accept_developer_for_job,job_apply
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',job_list),
    path('create',create_job),
    path('<int:id>/',job_detail),
    path('<int:id>/accept', accept_developer_for_job),
    path('<int:id>/apply/', job_apply),

]

urlpatterns  = format_suffix_patterns(urlpatterns)