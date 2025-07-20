from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class FoodPost(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='foodposts_posted'  # rename reverse relation
    )
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    dietary = models.CharField(max_length=200, blank=True)
    image1 = models.ImageField( null=True, blank=True)
    location = models.CharField(max_length=200)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    contact_method = models.CharField(max_length=100)
    special_instructions = models.TextField(blank=True)
    picked_up = models.BooleanField(default=False)
   
    def __str__(self):
        return self.name

