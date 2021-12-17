from django.shortcuts import render

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

def product(request):
    context = {

    }
    return render(request,"store/product.html",context)