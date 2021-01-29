from django.db import models

# Create your models here.
class Property(models.Model):
    address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=4)
    town = models.CharField(max_length=100)
    pic = models.ImageField(upload_to='pics')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)