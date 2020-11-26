from django.db import models

# Create your models here.

# main model for the produce management system


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

# class model for the aviable discount for this product section


class Offer(models.Model):
    code = models.CharField(max_length=10)
    discription = models.CharField(max_length=255)
    discount = models.FloatField()
