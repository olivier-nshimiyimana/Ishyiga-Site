from django.urls import path,include

from . import views


urlpatterns = [    
   
    path('music/',views.home, name='home'),
    # path('addition/',views.addition, name='addition'),
    path('', views.products, name='products'),
    path('', views.event, name='event')
    # path('')
]
