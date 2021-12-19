from django.urls import path

from . import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
    path('cart/',views.cart,name='cart'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('phones/',views.phones,name='phones'),
    path('laptops/',views.laptops,name='laptops'),
    path('essentials/',views.essentials,name='essentials'),
]