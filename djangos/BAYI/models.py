from django.db import models
from SSB.models import Products
# Create your models here.
class SideBarElements:
    id : int
    elementName : str
    order : int
    subElementsCount : int

class Customers (models.Model):
    customerName = models.CharField(max_length=100)
    customerName = models.CharField(max_length=50)
    orderedProduct = models.ForeignKey(
         Products, on_delete=models.CASCADE)
    orderAmount = models.IntegerField(default=0)
    orderDate = models.DateField()
    estimatedDelivery = models.DateField()