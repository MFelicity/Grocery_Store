from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request,"store_page/home.html")

def cart(request):
    return render (request,"store_page/cart.html")

def checkout(request):
    return render (request,"store_page/checkout.html")