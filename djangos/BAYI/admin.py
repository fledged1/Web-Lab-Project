from django.contrib import admin
from django import forms
from .models import Customers
from .models import CustomersOrders
# Register your models here.
admin.site.register(Customers)
admin.site.register(CustomersOrders)
