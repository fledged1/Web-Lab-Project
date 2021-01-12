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
    return render(request,'bayi_Index.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5})

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
    products = Products.objects.all()
    return render(request,'bayi_Urunler.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5,'products':products})

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
    return render(request,'bayi_Musteriler.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5,'customers':customers})
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
    orders = Orders.objects.all()
    return render(request,'bayi_Siparisler.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5,'orders':orders})

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
    return render(request,'bayi_MusteriSiparis.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5,})