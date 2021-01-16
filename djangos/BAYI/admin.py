from django.contrib import admin
from django import forms
from .models import Customers
from .models import CustomersOrders
from .models import PaymentMethods
from .models import Payment
from .models import Maintenance
# Register your models here.
admin.site.register(Customers)
admin.site.register(CustomersOrders)
admin.site.register(PaymentMethods)
admin.site.register(Payment)
admin.site.register(Maintenance)
