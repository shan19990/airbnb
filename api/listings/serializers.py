from rest_framework import serializers
from .models import *
from django.db.models import Avg

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseImageModel
        fields = "__all__"

class HouseSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True,required=False)
    reviews = ReviewSerializer(many=True ,required=False)
    main_image = serializers.ImageField(required=False)

    class Meta:
        model = HouseModel
        fields = ['id', 'owner', 'title', 'description', 'address', 'city', 'state', 'country', 'zip_code', 'latitude', 'longitude', 'bedrooms', 'bathrooms', 'price_per_night', 'embeded_url', 'main_image', 'images', 'reviews', 'average_rating']

    average_rating = serializers.SerializerMethodField()

    def get_average_rating(self, obj):
        return obj.reviews.aggregate(Avg('rating'))['rating__avg']
    
