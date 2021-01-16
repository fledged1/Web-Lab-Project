from django.db import models
from SSB.models import Products
from SSB.models import Orders
from SSB.models import Retailors
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
    def __str__(self):
        return self.customerName

class CustomersOrders (models.Model):
    orderName = models.CharField(max_length=100,verbose_name='Sipariş Adı')
    customer = models.ForeignKey(
        Customers,on_delete=models.DO_NOTHING,verbose_name='Müşteri'
    )
    orderAmount = models.IntegerField(default=0,verbose_name='Sipariş Miktarı')
    orderDate = models.DateField(verbose_name='Sipariş Tarihi')
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE,verbose_name="Ürün")
    estimatedDelivery = models.DateField(verbose_name='Tahmini Teslim Süresi')
    orderStatus = models.BooleanField(default=False,verbose_name='Tamamlandı')
    priceSold = models.FloatField(default=0,verbose_name='Satış Fiyatı')
    def __str__(self):
        return self.orderName
    def profit(self):
        return (self.priceSold * self.orderAmount) - (self.product.productPrice*self.orderAmount)


        
class PaymentMethods (models.Model):
    paymentName = models.CharField(max_length=100,verbose_name='Ödeme Yöntemi') 
    def __str__(self):
        return self.paymentName

class Payment (models.Model):
    paymentBayiName = models.CharField(max_length=100,verbose_name='Bayi Ödeme Adı')
    paymentAmount = models.FloatField(default=0,verbose_name='Ödeme Miktarı')
    retailor = models.ForeignKey(
         Retailors, on_delete=models.CASCADE,verbose_name='Bayi Adı',default='')
    order = models.ForeignKey(
        Orders, on_delete=models.CASCADE,verbose_name="Bayi Siparişleri")
    paymentName = models.ForeignKey(
        PaymentMethods, on_delete=models.CASCADE,verbose_name='Ödeme Yöntemi')
    paymentNot = models.TextField(max_length=100,verbose_name='Ödeme Notu')     
    def __str__(self):
        return self.paymentBayiName

class Maintenance (models.Model):
    customerMaintenanceName = models.CharField(max_length=100,verbose_name='Müşteri Adı')
    customer = models.ForeignKey(
        Customers,on_delete=models.DO_NOTHING,verbose_name='Müşteri'
    )
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE,verbose_name="Ürün")
    maintenanceDescription = models.TextField(max_length=100,verbose_name='Bakım Açıklaması')  
    maintenanceCost = models.FloatField(default=0,verbose_name='Bakım Maliyeti')
    def __str__(self):
        return self.customerMaintenanceName  