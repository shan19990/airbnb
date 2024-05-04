from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class BookingSerializers(generics.CreateAPIView):
    queryset = BookingModel
    serializer_class = BookingSerializer

class UserBookingListView(APIView):
    def get(self, request, user_id):
        try:
            bookings = BookingModel.objects.filter(user_id=user_id)
            serializer = BookingSerializer(bookings, many=True)
            return Response(serializer.data, status=200)
        except BookingModel.DoesNotExist:
            return Response({"error": "User bookings not found."}, status=400)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
class EditBookingView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookingModel.objects.all()
    serializer_class = BookingSerializer
    lookup_field = "id"

class UserBookingListView(generics.ListAPIView):
    serializer_class = BookingSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('house_owner')
        return BookingModel.objects.filter(user_id=user_id)