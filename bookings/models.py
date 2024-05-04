from django.db import models
from django.contrib.auth.models import User
from listings.models import HouseModel

STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('negotiation', 'Negotiation'),
        ('going_on', 'Going On'),
        ('ended', 'Ended'),
    ]

class BookingModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    house = models.ForeignKey(HouseModel, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    guests = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    

    def __str__(self):
        return f"Booking #{self.pk} - {self.user.username} - {self.house.title}"
    
    def save(self, *args, **kwargs):
        num_nights = (self.check_out_date - self.check_in_date).days + 1
        self.total_price = self.price_per_night * num_nights
        super().save(*args, **kwargs)

