from django.db import models
from SSB.models import Products
from SSB.models import Orders
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

class CustomersOrders (models.Model):
    orderName = models.CharField(max_length=100,verbose_name='Sipariş Adı')
    customerName = models.CharField(max_length=100, verbose_name='Müşteri Adı, Soyadı')
    orderAmount = models.IntegerField(default=0,verbose_name='Sipariş Miktarı')
    orderDate = models.DateField(verbose_name='Sipariş Tarihi')
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE,verbose_name="Ürün")
    estimatedDelivery = models.DateField(verbose_name='Tahmini Teslim Süresi')
    orderStatus = models.BooleanField(default=False,verbose_name='Tamamlandı')
    def str(self):
        return self.orderName
    def orderTotal(self):
        return self.orderAmount * self.Products.productPrice