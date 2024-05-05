# views.py

from rest_framework import generics
from .models import ChatRoomModel, MessageModel
from .serializers import ChatRoomDetailSerializer, ChatRoomCreateSerializer

class ChatRoomCreateAPIView(generics.CreateAPIView):
    queryset = ChatRoomModel.objects.all()
    serializer_class = ChatRoomCreateSerializer

class ChatRoomDetailAPIView(generics.RetrieveAPIView):
    queryset = ChatRoomModel.objects.all()
    serializer_class = ChatRoomDetailSerializer
