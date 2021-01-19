from django.shortcuts import render
from .models import SideBarElements
from django.http import HttpResponse
from SSB.models import Products
from SSB.models import Orders
from SSB.models import Materials
from BAYI.models import Customers
from BAYI.models import CustomersOrders
from BAYI.models import Payment
from BAYI.models import Maintenance
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from BAYI.serializers import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = CustomersOrders.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
# Create your views here.

def home(request):
    #///////SideBar Elements\\\\\\\\
    element1 = SideBarElements()
    element1.elementName = 'Anasayfa'
    element2 = SideBarElements()
    element2.elementName = 'Ürünler'
    element3 = SideBarElements()
    element3.elementName = 'Siparişler'
    element4 = SideBarElements()
    element4.elementName = 'Müşteri Siparişleri'
    element5 = SideBarElements()
    element5.elementName = 'Siparişlerim'
    element6 = SideBarElements()
    element6.elementName = 'Müşteriler'
    element7 = SideBarElements()
    element7.elementName = 'Bakım'
    element8 = SideBarElements()
    element8.elementName = 'Ödemelerim'
    element9 = SideBarElements()
    element9.elementName = 'Finans'

    names = []
    data = []
    queryset = Products.objects.order_by('-estimatedDelivery')[:5]
    for product in queryset:
        names.append(product.productName)
        data.append(product.estimatedDelivery)

    return render(request,'bayi_Index.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5, 'element6':element6, 'element7':element7,'element8':element8, 'element9':element9,'names':names,'data':data})

def Urunler(request):
    element1 = SideBarElements()
    element1.elementName = 'Anasayfa'
    element2 = SideBarElements()
    element2.elementName = 'Ürünler'
    element3 = SideBarElements()
    element3.elementName = 'Siparişler'
    element4 = SideBarElements()
    element4.elementName = 'Müşteri Siparişleri'
    element5 = SideBarElements()
    element5.elementName = 'Siparişlerim'
    element6 = SideBarElements()
    element6.elementName = 'Müşteriler'
    element7 = SideBarElements()
    element7.elementName = 'Bakım'
    element8 = SideBarElements()
    element8.elementName = 'Ödemelerim'
    element9 = SideBarElements()
    element9.elementName = 'Finans'
    products = Products.objects.all()
    return render(request,'bayi_Urunler.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5,
     'element6':element6, 'element7':element7,'element8':element8, 'element9':element9, 'products':products})

def Musteriler(request):
    element1 = SideBarElements()
    element1.elementName = 'Anasayfa'
    element2 = SideBarElements()
    element2.elementName = 'Ürünler'
    element3 = SideBarElements()
    element3.elementName = 'Siparişler'
    element4 = SideBarElements()
    element4.elementName = 'Müşteri Siparişleri'
    element5 = SideBarElements()
    element5.elementName = 'Siparişlerim'
    element6 = SideBarElements()
    element6.elementName = 'Müşteriler'
    element7 = SideBarElements()
    element7.elementName = 'Bakım'
    element8 = SideBarElements()
    element8.elementName = 'Ödemelerim'
    element9 = SideBarElements()
    element9.elementName = 'Finans'
    customers = Customers.objects.all()
    return render(request,'bayi_Musteriler.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5, 'element6':element6, 'element7':element7,'element8':element8, 'element9':element9,'customers':customers})

def Siparisler(request):
    element1 = SideBarElements()
    element1.elementName = 'Anasayfa'
    element2 = SideBarElements()
    element2.elementName = 'Ürünler'
    element3 = SideBarElements()
    element3.elementName = 'Siparişler'
    element4 = SideBarElements()
    element4.elementName = 'Müşteri Siparişleri'
    element5 = SideBarElements()
    element5.elementName = 'Siparişlerim'
    element6 = SideBarElements()
    element6.elementName = 'Müşteriler'
    element7 = SideBarElements()
    element7.elementName = 'Bakım'
    element8 = SideBarElements()
    element8.elementName = 'Ödemelerim'
    element9 = SideBarElements()
    element9.elementName = 'Finans'
    orders = Orders.objects.all()
    return render(request,'bayi_Siparisler.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5, 'element6':element6, 'element7':element7,'element8':element8, 'element9':element9,'orders':orders})

def MusteriSiparisler(request):
    element1 = SideBarElements()
    element1.elementName = 'Anasayfa'
    element2 = SideBarElements()
    element2.elementName = 'Ürünler'
    element3 = SideBarElements()
    element3.elementName = 'Siparişler'
    element4 = SideBarElements()
    element4.elementName = 'Müşteri Siparişleri'
    element5 = SideBarElements()
    element5.elementName = 'Siparişlerim'
    element6 = SideBarElements()
    element6.elementName = 'Müşteriler'
    element7 = SideBarElements()
    element7.elementName = 'Bakım'
    element8 = SideBarElements()
    element8.elementName = 'Ödemelerim'
    element9 = SideBarElements()
    element9.elementName = 'Finans'
    customersorders = CustomersOrders.objects.all()
    return render(request,'bayi_MusteriSiparis.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5, 'element6':element6, 'element7':element7,'element8':element8, 'element9':element9,'customersorders':customersorders})

def Finans(request):
    element1 = SideBarElements()
    element1.elementName = 'Anasayfa'
    element2 = SideBarElements()
    element2.elementName = 'Ürünler'
    element3 = SideBarElements()
    element3.elementName = 'Siparişler'
    element4 = SideBarElements()
    element4.elementName = 'Müşteri Siparişleri'
    element5 = SideBarElements()
    element5.elementName = 'Siparişlerim'
    element6 = SideBarElements()
    element6.elementName = 'Müşteriler'
    element7 = SideBarElements()
    element7.elementName = 'Bakım'
    element8 = SideBarElements()
    element8.elementName = 'Ödemelerim'
    element9 = SideBarElements()
    element9.elementName = 'Finans'
    
    customersorders = CustomersOrders.objects.all()
    names = []
    data = []
    queryset = Products.objects.order_by('-productPrice')[:5]
    for product in queryset:
        names.append(product.productName)
        data.append(product.productPrice)

    names1 = []
    data1 = []
    queryset1 = Products.objects.order_by('-productPrice')[:10]
    for product in queryset1:
        names1.append(product.productName)
        data1.append(product.productPrice)
    return render(request,'bayi_Finans.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,
    'element5':element5, 'element6':element6, 'element7':element7,'element8':element8, 'element9':element9, 'names': names,'data': data,
    'names1': names1,'data1': data1,'customersorders':customersorders})

def Odemelerim(request):
    element1 = SideBarElements()
    element1.elementName = 'Anasayfa'
    element2 = SideBarElements()
    element2.elementName = 'Ürünler'
    element3 = SideBarElements()
    element3.elementName = 'Siparişler'
    element4 = SideBarElements()
    element4.elementName = 'Müşteri Siparişleri'
    element5 = SideBarElements()
    element5.elementName = 'Siparişlerim'
    element6 = SideBarElements()
    element6.elementName = 'Müşteriler'
    element7 = SideBarElements()
    element7.elementName = 'Bakım'
    element8 = SideBarElements()
    element8.elementName = 'Ödemelerim'
    element9 = SideBarElements()
    element9.elementName = 'Finans'
    payment = Payment.objects.all()
    return render(request,'bayi_Odemelerim.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5, 'element6':element6, 'element7':element7,'element8':element8, 'element9':element9, 'payment':payment})

def Bakım(request):
    element1 = SideBarElements()
    element1.elementName = 'Anasayfa'
    element2 = SideBarElements()
    element2.elementName = 'Ürünler'
    element3 = SideBarElements()
    element3.elementName = 'Siparişler'
    element4 = SideBarElements()
    element4.elementName = 'Müşteri Siparişleri'
    element5 = SideBarElements()
    element5.elementName = 'Siparişlerim'
    element6 = SideBarElements()
    element6.elementName = 'Müşteriler'
    element7 = SideBarElements()
    element7.elementName = 'Bakım'
    element8 = SideBarElements()
    element8.elementName = 'Ödemelerim'
    element9 = SideBarElements()
    element9.elementName = 'Finans'
    maintenance = Maintenance.objects.all()
    return render(request,'bayi_Bakım.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5, 'element6':element6, 'element7':element7,'element8':element8, 'element9':element9, 'maintenance':maintenance})
