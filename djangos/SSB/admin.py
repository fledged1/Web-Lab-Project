from django.contrib import admin
from django import forms
from .models import Users
from .models import Products
from .models import Materials
from .models import Recipes
from .models import Retailors
from .models import Orders
# Register your models here.

admin.site.register(Users)
admin.site.register(Recipes)
admin.site.register(Retailors)

class ProductsAdmin(admin.ModelAdmin):
    fields=['productName','productImage','productDescription','productSerial','productPrice','estimatedDelivery']
admin.site.register(Products,ProductsAdmin)

    
class OrdersAdmin(admin.ModelAdmin):
    fields=['orderName','retailor','orderedProduct','orderAmount','orderDate','estimatedDelivery']
admin.site.register(Orders,OrdersAdmin)

class MaterialsAdmin(admin.ModelAdmin):
    fields=['materialName','materialUnit','materialStockCount','estimatedSupply','tresholdValue','unitPrice','lastOrder']
admin.site.register(Materials,MaterialsAdmin)