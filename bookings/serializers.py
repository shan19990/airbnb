from rest_framework import serializers
from .models import *

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingModel
        fields = "__all__"
        extra_kwargs = {
            'total_price': {'required': False}
        }

