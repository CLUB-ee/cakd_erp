"""ERP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
import template.views

app_name = 'template'

urlpatterns = [
    path('', template.views.dash, name='dash'),
    path('orders/', template.views.orders, name='orders'),
    path('orderapp/', template.views.orderapp, name='orderapp'),
    path('stock/', template.views.stock, name='stock'),
    path('sale/', template.views.sale, name='sale'),
    path('my/', template.views.my, name='my'),
    path('login/', template.views.login, name='login'),
    path('register/', template.views.register, name='register'),
]
