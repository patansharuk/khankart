from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    updated_date = models.DateTimeField()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)