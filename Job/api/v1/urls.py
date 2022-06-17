from django.urls import path
from Job.api.v1 import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.job_list),
    path('create', views.create_job),
    path('<int:id>/', views.job_detail),
    path('<int:id>/accept/', views.accept_developer_for_job),
    path('<int:id>/apply/', views.job_apply),
    path('<int:id>/getApplied/', views.get_applied_developers_job),

]

urlpatterns  = format_suffix_patterns(urlpatterns)