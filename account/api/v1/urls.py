from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import get_notifications, signupUser, signupCompany, list_user, list_company, user_details, company_details, List, details, \
    update, delete, logout_user,get_all_finished_jobs

app_name = 'job-system-rest-v1'

urlpatterns = [
    path('rest_login/', obtain_auth_token),
    path('signupUser/', signupUser, name='signupUser'),
    path('signupCompany/', signupCompany, name='signupCompany'),
    # path('list_user/', list_user, name='list_user'),
    # path('list_company/', list_company, name='list_company'),
    path('List/<str:user_type>', List, name='List'),
    path('user_details/', user_details, name='user_details'),
    # path('company_details/<int:company_id>', company_details, name='company_details'),
    path('details/<str:user_type>/<int:ids>', details, name='details'),
    path('update/', update, name='update'),
    path('delete/<str:user_type>/<int:ids>', delete, name='delete'),
    path('logout_user',logout_user,name='logout_user'),
    path('notifications',get_notifications,name='notifications'),
    path('<int:id>/get_all_finished_jobs',get_all_finished_jobs ,name='get_all_finished_jobs')




]