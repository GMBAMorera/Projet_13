from product.models import Product
from django.db import models
from product.models import Product
from constants import ORDER_STATUS

# Create your models here.

class Order(models.Model):
    status = models.CharField(max_length=2, choices=ORDER_STATUS)


class OrderedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)