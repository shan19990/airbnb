# urls.py

from django.urls import path
from .views import ChatRoomCreateAPIView, ChatRoomDetailAPIView

urlpatterns = [
    path('chatrooms/create/', ChatRoomCreateAPIView.as_view(), name='chatroom-create'),
    path('chatrooms/<int:pk>/', ChatRoomDetailAPIView.as_view(), name='chatroom-detail'),
]
