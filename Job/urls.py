from django.contrib import admin
from django.urls import path
from Job import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('',views.job_list),
    path('<int:id>/' , views.job_detail)
]

urlpatterns  = format_suffix_patterns(urlpatterns)