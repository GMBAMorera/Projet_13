from django.db import models

# Create your models here.


class Product(models.Model):
    off_the_shelf_price = models.DecimalField(max_digits=10, decimal_places=2)
    production_cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.DecimalField(max_digits=10, decimal_places=2)
    stock_unit = models.CharField(max_length=25)
