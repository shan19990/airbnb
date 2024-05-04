"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('house/', HouseListView.as_view(), name="houses"),
    path('house/add/', HouseCreateView.as_view(), name="addhouse"),
    path('house/<int:id>/', HouseDetailView.as_view(), name="edithouse"),
    path('house/image/add/', HousePhotosCreateView.as_view(), name="addimage"),
    path('house/image/edit/<int:id>/', HousePhotosEditView.as_view(), name="editimage"),
    path('house/review/add/', HouseReviewCreateView.as_view(), name="addreview"),
    path('house/review/edit/<int:id>/', HouseReviewEditView.as_view(), name="editreview"),
]
