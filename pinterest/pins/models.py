from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)

class Category(models.Model):
    name = models.CharField(max_length=30)
    
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length=30)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)