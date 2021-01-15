from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bayi_Urunler.html',views.Urunler,name='Ürünler'),
    path('bayi_Musteriler.html',views.Musteriler,name='Müşteriler'),
    path('bayi_Siparisler.html',views.Siparisler,name='Siparişler'),
    path('bayi_MusteriSiparis.html',views.MusteriSiparisler,name='Müşteri Siparişleri'),
    path('bayi_Finans.html',views.Finans,name='Finans'),
]