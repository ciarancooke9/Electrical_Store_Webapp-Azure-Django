from django.shortcuts import render

from . models import Category, Product

# Create your views here.
def index(request):
    context = {

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
    products = Product.objects.get(category='Phones')
    context = {
        'product': products.objects.all()
    }
    return render(request,"store/phones.html",context)