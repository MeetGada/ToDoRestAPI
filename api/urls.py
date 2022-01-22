from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # link for registration
    path('register/', userRegister.as_view(), name='userRegister'),
    # this link will send all the tasks of the logged-in user
    path('all-tasks/', taskList.as_view(), name='userDashboard'),
    # this link will is used to create task 
    path('create-work/', addWork.as_view(), name='addWork'),
    # Here, using the primary-key (pk) work can be updated or deleted
    path('work-edit/<int:pk>', edit_task.as_view(), name='editWork'),
    # sending token for login using token authentication
    path('login/', obtain_auth_token, name='login'),
    # logout link
    path('logout/', logoutUser.as_view(), name='userLogout'),
]