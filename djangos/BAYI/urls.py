from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('bayi_Urunler.html',views.Urunler,name='Ürünler'),
]