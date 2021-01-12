from django.shortcuts import render
from .models import SideBarElements
from django.http import HttpResponse
from SSB.models import Products
from SSB.models import Orders
from BAYI.models import Customers
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
    element7.elementName = 'Finans'
    return render(request,'bayi_Index.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5,'element6':element6,'element7':element7})

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
    element7.elementName = 'Finans'
    products = Products.objects.all()
    return render(request,'bayi_Urunler.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5,'element6':element6,'element7':element7, 'products':products})

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
    element7.elementName = 'Finans'
    return render(request,'bayi_Musteriler.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5, 'element6':element6, 'element7':element7,'customers':customers})

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
    element7.elementName = 'Finans'
    orders = Orders.objects.all()
    return render(request,'bayi_Siparisler.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5, 'element6':element6, 'element7':element7,'orders':orders})

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
    element7.elementName = 'Finans'
    return render(request,'bayi_MusteriSiparis.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5, 'element6':element6, 'element7':element7})

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
    element7.elementName = 'Finans'
    customers = Customers.objects.all()
    return render(request,'bayi_MusteriSiparis.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5, 'element6':element6, 'element7':element7,'customers':customers})