from django.db import models

# Create your models here.


class Users (models.Model):
    userName = models.CharField(max_length=50)
    userPassword = models.CharField(max_length=50)
    userPermissions : models.IntegerField(default=0)
class SideBarElements:
    id : int
    elementName : str
    order : int
    subElementsCount : int
class Products (models.Model):
    productName = models.CharField(max_length=100,verbose_name='Ürün Adı') 
    productImage = models.ImageField(upload_to='pics',verbose_name='Ürün Resmi')
    productDescription = models.TextField(verbose_name='Açıklama')
    productSerial = models.IntegerField(default=0,verbose_name='Sipariş Numarası')
    productPrice = models.IntegerField(default=0,verbose_name='Fiyat')
    estimatedDelivery = models.IntegerField(default=0,verbose_name='Tahmini Teslim Süresi')
    productStock = models.IntegerField(default=0,verbose_name='Stok Adedi')
    def __str__(self):
        return self.productName
class Materials (models.Model):
    materialName = models.CharField(max_length=100,verbose_name='Hammadde Adı')
    materialUnit = models.CharField(max_length=100,verbose_name='Birim')
    materialStockCount = models.FloatField(default=0,verbose_name='Stok Miktarı')
    estimatedSupply = models.IntegerField(default=0,verbose_name='Tahmini Temin Süresi')
    tresholdValue = models.FloatField(default=0,verbose_name='Eşik Değer')
    unitPrice = models.FloatField(default=0,verbose_name='Birim Fiyat')
    lastOrder = models.DateField(verbose_name='Son Sipariş')
    def __str__(self):
        return self.materialName
class Recipes (models.Model):
    recipeName = models.CharField(max_length=100)
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE)
    recipeCreationDate = models.DateField()
    recipeSingleProductPrice = models.FloatField(default=0)
    recipeAdditionalCosts = models.FloatField(default=0)
    recipeProductionCount = models.IntegerField(default=0)
    def __str__(self):
        return self.recipeName
class Retailors (models.Model):
    retailorName = models.CharField(default='',max_length=100,verbose_name='Bayi Adı')
    retailorPhone = models.CharField(max_length=50,verbose_name='Telefon')
    retailorAddress = models.TextField(verbose_name='Adres')
    retailorEndorsement = models.FloatField(default=0,verbose_name='Ciro (TL)')
    def __str__(self):
        return self.retailorName

class Orders (models.Model):
    orderName = models.CharField(max_length=100,verbose_name='Sipariş Adı')
    retailor = models.ForeignKey(
         Retailors, on_delete=models.CASCADE,verbose_name='Bayi Adı',default='')
    orderedProduct = models.ForeignKey(
         Products,related_name='author_blogs', on_delete=models.CASCADE,verbose_name='Ürün')
    orderAmount = models.IntegerField(default=0,verbose_name='Sipariş Miktarı')
    orderDate = models.DateField(verbose_name='Sipariş Tarihi')
    estimatedDelivery = models.DateField(verbose_name='Tahmini Teslim Süresi')
    def __str__(self):
        return self.orderName
    def orderTotal(self):
        return self.orderAmount * self.orderedProduct.productPrice


