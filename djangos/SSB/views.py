from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import SideBarElements
from .models import Products
from .models import Materials
from .models import Recipes
from .models import Orders
from .models import Retailors
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from BAYI.models import Payment
from BAYI.models import PaymentMethods
# Create your views here.
    
def index(request):

    
   
   
    #///////SideBar Elements\\\\\\\\
    element1 = SideBarElements()
    element1.elementName = 'Anasayfa'
    element2 = SideBarElements()
    element2.elementName = 'Ürünler'
    element3 = SideBarElements()
    element3.elementName = 'Hammaddeler'
    element4 = SideBarElements()
    element4.elementName = 'Reçeteler'
    element5 = SideBarElements()
    element5.elementName = 'Siparişler'
    element6 = SideBarElements()
    element6.elementName = 'Bayiler'
    element7 = SideBarElements()
    element7.elementName = 'Finans'
    

    materials = Materials.objects.all()
    #piechart
    names = []
    data = []
    queryset = Materials.objects.order_by('-materialStockCount')[:10]
    for material in queryset:
        names.append(material.materialName)
        data.append(material.materialStockCount)

    retailorCount = Retailors.objects.count
    ordersCount = Orders.objects.count

    
    return render(request,'index.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5,'element6':element6,'element7':element7,'names': names,'data': data,'retailorCount':retailorCount,'ordersCount':ordersCount,'materials':materials})


def hammaddeler(request):
    element1 = SideBarElements()
    element1.elementName = 'Anasayfa'
    element2 = SideBarElements()
    element2.elementName = 'Ürünler'
    element3 = SideBarElements()
    element3.elementName = 'Hammaddeler'
    element4 = SideBarElements()
    element4.elementName = 'Reçeteler'
    element5 = SideBarElements()
    element5.elementName = 'Siparişler'
    element6 = SideBarElements()
    element6.elementName = 'Bayiler'
    element7 = SideBarElements()
    element7.elementName = 'Finans'

    
   
    materials = Materials.objects.all()
    
    return render(request,'hammaddeler.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5,'element6':element6,'element7':element7,'materials':materials,})

def urunler(request):
    element1 = SideBarElements()
    element1.elementName = 'Anasayfa'
    element2 = SideBarElements()
    element2.elementName = 'Ürünler'
    element3 = SideBarElements()
    element3.elementName = 'Hammaddeler'
    element4 = SideBarElements()
    element4.elementName = 'Reçeteler'
    element5 = SideBarElements()
    element5.elementName = 'Siparişler'
    element6 = SideBarElements()
    element6.elementName = 'Bayiler'
    element7 = SideBarElements()
    element7.elementName = 'Finans'

    materials = Materials.objects.all()

    products = Products.objects.all()

    return render(request,'urunler.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5,'element6':element6,'element7':element7,'products':products,'materials':materials})

def receteler(request):
    element1 = SideBarElements()
    element1.elementName = 'Anasayfa'
    element2 = SideBarElements()
    element2.elementName = 'Ürünler'
    element3 = SideBarElements()
    element3.elementName = 'Hammaddeler'
    element4 = SideBarElements()
    element4.elementName = 'Reçeteler'
    element5 = SideBarElements()
    element5.elementName = 'Siparişler'
    element6 = SideBarElements()
    element6.elementName = 'Bayiler'
    element7 = SideBarElements()
    element7.elementName = 'Finans'

    materials = Materials.objects.all()
    
    
    recipes = Recipes.objects.all()
   
    

    return render(request,'receteler.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5,'element6':element6,'element7':element7,'recipes':recipes,'materials':materials})

def recetehammaddeler(request):
    element1 = SideBarElements()
    element1.elementName = 'Anasayfa'
    element2 = SideBarElements()
    element2.elementName = 'Ürünler'
    element3 = SideBarElements()
    element3.elementName = 'Hammaddeler'
    element4 = SideBarElements()
    element4.elementName = 'Reçeteler'
    element5 = SideBarElements()
    element5.elementName = 'Siparişler'
    element6 = SideBarElements()
    element6.elementName = 'Bayiler'
    element7 = SideBarElements()
    element7.elementName = 'Finans'

    recipes = Recipes.objects.all()
   
    materials = Materials.objects.all()

    return render(request,'recetehammaddeler.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5,'element6':element6,'element7':element7,'recipes':recipes,'materials':materials})


def siparisler(request):
    element1 = SideBarElements()
    element1.elementName = 'Anasayfa'
    element2 = SideBarElements()
    element2.elementName = 'Ürünler'
    element3 = SideBarElements()
    element3.elementName = 'Hammaddeler'
    element4 = SideBarElements()
    element4.elementName = 'Reçeteler'
    element5 = SideBarElements()
    element5.elementName = 'Siparişler'
    element6 = SideBarElements()
    element6.elementName = 'Bayiler'
    element7 = SideBarElements()
    element7.elementName = 'Finans'

    materials = Materials.objects.all()
    orders = Orders.objects.all()    

    
    return render(request,'siparisler.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5,'element6':element6,'element7':element7,'orders':orders,'materials':materials})

def bayiler(request):
    element1 = SideBarElements()
    element1.elementName = 'Anasayfa'
    element2 = SideBarElements()
    element2.elementName = 'Ürünler'
    element3 = SideBarElements()
    element3.elementName = 'Hammaddeler'
    element4 = SideBarElements()
    element4.elementName = 'Reçeteler'
    element5 = SideBarElements()
    element5.elementName = 'Siparişler'
    element6 = SideBarElements()
    element6.elementName = 'Bayiler'
    element7 = SideBarElements()
    element7.elementName = 'Finans'

    
    materials = Materials.objects.all()
    retailors = Retailors.objects.all()   
    
    return render(request,'bayiler.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5,'element6':element6,'element7':element7,'retailors':retailors,'materials':materials})

def siparisgecmisleri(request):
    element1 = SideBarElements()
    element1.elementName = 'Anasayfa'
    element2 = SideBarElements()
    element2.elementName = 'Ürünler'
    element3 = SideBarElements()
    element3.elementName = 'Hammaddeler'
    element4 = SideBarElements()
    element4.elementName = 'Reçeteler'
    element5 = SideBarElements()    
    element5.elementName = 'Siparişler'
    element6 = SideBarElements()
    element6.elementName = 'Bayiler'
    element7 = SideBarElements()
    element7.elementName = 'Finans'
    

    materials = Materials.objects.all()
    query = Orders.objects.filter(retailor__exact = 1)
    
    return render(request,'siparisgecmisleri.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5,'element6':element6,'element7':element7,'query':query,'materials':materials})

def finans(request):
    element1 = SideBarElements()
    element1.elementName = 'Anasayfa'
    element2 = SideBarElements()
    element2.elementName = 'Ürünler'
    element3 = SideBarElements()
    element3.elementName = 'Hammaddeler'
    element4 = SideBarElements()
    element4.elementName = 'Reçeteler'
    element5 = SideBarElements()
    element5.elementName = 'Siparişler'
    element6 = SideBarElements()
    element6.elementName = 'Bayiler'
    element7 = SideBarElements()
    element7.elementName = 'Finans'
    
    names = []
    data = []
    queryset = Products.objects.order_by('-productPrice')[:5]
    for product in queryset:
        names.append(product.productName)
        data.append(product.productPrice)

    names1 = []
    data1 = []
    queryset1 = Materials.objects.order_by('-materialStockCount')[:10]
    for material in queryset1:
        names1.append(material.materialName)
        data1.append(material.materialStockCount)

    payment = Payment.objects.all()
    materials = Materials.objects.all()

    return render(request,'finans.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5,'element6':element6,'element7':element7,
    'names': names,'data': data,'names1': names1,'data1': data1,'payment':payment,'materials':materials})