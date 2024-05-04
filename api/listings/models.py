from django.db import models
from django.contrib.auth.models import User

class HouseModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    latitude = models.FloatField(blank=True,null=True)
    longitude = models.FloatField(blank=True,null=True)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    embeded_url = models.CharField(max_length=10000, blank=True,null=True)
    main_image = models.ImageField(upload_to="main_image/")

    def __str__(self):
        return self.title

class HouseImageModel(models.Model):
    house = models.ForeignKey(HouseModel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="house_images/")

    def __str__(self):
        return f"Image for {self.house.title}"

class ReviewModel(models.Model):
    house = models.ForeignKey(HouseModel, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.house.title}"
