from django.shortcuts import render

def dash(request):
    return render(request, 'dash.html')

def orders(request):
    return render(request, 'orders.html')

def orderapp(request):
    return render(request, 'orderapp.html')

def stock(request):
    return render(request, 'stock.html')

def sale(request):
    return render(request, 'sale.html')

def my(request):
    return render(request, 'my.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
# Create your views here.
