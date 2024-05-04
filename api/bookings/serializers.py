from rest_framework import serializers
from .models import *

class BookingSerializer(serializers.ModelSerializer):

    house_owner = serializers.SerializerMethodField()

    class Meta:
        model = BookingModel
        fields = "__all__"
        extra_kwargs = {
            'total_price': {'required': False}
        }

    def get_house_owner(self, obj):
        return obj.house.owner.id if obj.house.owner else None

