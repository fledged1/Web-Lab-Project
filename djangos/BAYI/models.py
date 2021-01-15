from django.db import models
from SSB.models import Products
# Create your models here.
class SideBarElements:
    id : int
    elementName : str
    order : int
    subElementsCount : int

class Customers (models.Model):
    customerName = models.CharField(max_length=100, verbose_name='Müşteri Adı, Soyadı')
    customerPhone = models.CharField(max_length=50,verbose_name='Müşteri Telefonu')
    customerMail = models.CharField(max_length=50,verbose_name='Müşteri Maili')
    customerAddress = models.CharField(max_length=50,verbose_name='Müşteri Adresi')