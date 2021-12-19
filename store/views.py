from django.shortcuts import render

from . models import Category, Product

# Create your views here.
def index(request):
    phones = Product.objects.filter(category__name='Phones')
    laptops = Product.objects.filter(category__name='Laptops')
    essentials = Product.objects.filter(category__name='Household Essentials')
    context = {
        'phones': phones,
        'laptops': laptops,
        'essentials': essentials,
    }
    return render(request,"store/index.html",context)

def cart(request):
    context = {

    }
    return render(request,"store/cart.html",context)

def login(request):
    context = {

    }
    return render(request,"store/login.html",context)


def signup(request):
    context = {

    }
    return render(request,"store/signup.html",context)

def phones(request):
    products = Product.objects.filter(category__name='Phones')
    context = {
        'product': products,
    }
    return render(request,"store/phones.html",context)

def laptops(request):
    products = Product.objects.filter(category__name='Laptops')
    context = {
        'product': products,
    }
    return render(request,"store/laptops.html",context)

def essentials(request):
    products = Product.objects.filter(category__name='Household Essentials')
    context = {
        'product': products,
    }
    return render(request,"store/essentials.html",context)