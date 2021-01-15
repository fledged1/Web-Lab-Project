from django.contrib.auth.models import Group
from BAYI.models import Customers
from rest_framework import serializers

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customers
        fields = ['id', 'customerName','customerPhone','customerMail','customerAddress']