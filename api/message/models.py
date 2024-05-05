# models.py

from django.db import models
from django.contrib.auth.models import User

class ChatRoomModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MessageModel(models.Model):
    room = models.ForeignKey(ChatRoomModel, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.username} - {self.content}'
