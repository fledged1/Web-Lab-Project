from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('hammaddeler.html',views.hammaddeler,name='hammaddeler'),
    path('urunler.html',views.urunler,name='urunler'),
    path('receteler.html',views.receteler,name='receteler'),
    path('siparisler.html',views.siparisler,name='siparisler'),
    path('bayiler.html',views.bayiler,name='bayiler'),
    path('siparisgecmisleri.html',views.siparisgecmisleri,name='siparisgecmisleri'),
    path('finans.html',views.finans,name='finans'),
    
]