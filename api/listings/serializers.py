from rest_framework import serializers
from .models import HouseModel

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseModel
        fields = "__all__"

        extra_kwargs = {
            'embeded_url': {'required': False},
            'latitude': {'required': False},
            'longitude': {'required': False},
        }

        def to_internal_value(self, data):
            # Convert double quotes to single quotes
            data['embeded_url'] = data.get('embeded_url').replace('"', "'")
            return super().to_internal_value(data)