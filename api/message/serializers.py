# serializers.py

from rest_framework import serializers
from .models import ChatRoomModel, MessageModel

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')

    class Meta:
        model = MessageModel
        fields = ['id', 'sender', 'content', 'timestamp']

class ChatRoomDetailSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = ChatRoomModel
        fields = ['id', 'name', 'messages']

class ChatRoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoomModel
        fields = ['id', 'name']
