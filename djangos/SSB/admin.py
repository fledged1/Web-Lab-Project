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
admin.site.register(Retailors)

class RecipesAdmin(admin.ModelAdmin):
    fields=['recipeName','product','recipeCreationDate','materials','recipeSingleProductPrice','recipeAdditionalCosts','recipeProductionCount']
admin.site.register(Recipes,RecipesAdmin)


class ProductsAdmin(admin.ModelAdmin):
    fields=['productName','productImage','productDescription','productSerial','productPrice','estimatedDelivery','productStock','carePeriod']
admin.site.register(Products,ProductsAdmin)

    
class OrdersAdmin(admin.ModelAdmin):
    fields=['orderName','retailor','orderedProduct','orderAmount','orderDate','estimatedDelivery','orderStatus']
admin.site.register(Orders,OrdersAdmin)

class MaterialsAdmin(admin.ModelAdmin):
    fields=['materialName','materialUnit','materialStockCount','estimatedSupply','tresholdValue','unitPrice','lastOrder']
admin.site.register(Materials,MaterialsAdmin)