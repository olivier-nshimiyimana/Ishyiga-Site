from django.urls import path,include

from . import views


urlpatterns = [    
   
    # path('',views.user_login, name='user_login'),
    # path('login/', views.user_login, name='login'),
    path('', views.user_login, name='user_login'),
    # path('logout/', views.user_logout, name='logout'),
   
]
