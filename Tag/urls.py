from django.contrib import admin
from django.urls import path
from Tag import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('',views.tag_list),
    path('<int:id>/' , views.tag_detail)
]

urlpatterns  = format_suffix_patterns(urlpatterns)