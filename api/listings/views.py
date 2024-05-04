from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics

class HouseListView(generics.ListAPIView):
    queryset = HouseModel.objects.all()
    serializer_class = HouseSerializer

class HouseCreateView(generics.CreateAPIView):
    queryset = HouseModel.objects.all()
    serializer_class = HouseSerializer

class HouseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HouseModel.objects.all()
    serializer_class = HouseSerializer
    lookup_field = "id"
