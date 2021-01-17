from django.contrib.auth.models import Group
from BAYI.models import CustomersOrders
from rest_framework import serializers

class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CustomersOrders
        fields = ('id', 'orderName','priceSold','estimatedDelivery','orderDate','orderAmount')
