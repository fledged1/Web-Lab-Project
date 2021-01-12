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
    customerPhone = models.CharField(max_length=50)
    customerMail = models.CharField(max_length=50)
    customerAddress = models.CharField(max_length=50)
    retailorEndorsement = models.FloatField(default=0,verbose_name='Ciro (TL)')