
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UsersDetailView.as_view(), name="userslist"),
    path('user/<int:id>/', UserDetailView.as_view(), name="userdetail"),
    path('user/password/<int:id>/', UserUpdatePasswordView.as_view(), name="userpasswordupdate"),
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
]
