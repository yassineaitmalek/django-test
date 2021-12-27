from django.db import models

class Product(models.Model) :
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    summary = models.TextField(default='yaay')
    featured = models.BooleanField()
# Create your models here.
