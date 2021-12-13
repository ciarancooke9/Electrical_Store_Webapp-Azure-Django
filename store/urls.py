from django.urls import path

from . import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
    path('cart/',views.carparks,name='cart'),
    path('signup/',views.carparks,name='signup'),
    path('login/',views.carparks,name='login'),
]