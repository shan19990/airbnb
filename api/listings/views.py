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

class HousePhotosCreateView(generics.CreateAPIView):
    queryset = HouseImageModel.objects.all()
    serializer_class = ImageSerializer

class HousePhotosEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HouseImageModel.objects.all()
    serializer_class = ImageSerializer
    lookup_field = "id"

class HouseReviewCreateView(generics.CreateAPIView):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer

class HouseReviewEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = "id"