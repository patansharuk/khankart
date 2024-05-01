from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    updated_date = models.DateField()
