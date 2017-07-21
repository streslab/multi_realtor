from django.db import models

# Create your models here.

class House(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    beds = models.CharField(max_length=100)
    baths = models.CharField(max_length=100)
    sqft = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
