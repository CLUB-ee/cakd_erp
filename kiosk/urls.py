
from django.urls import path, include
from . import views

app_name = 'kiosk'

urlpatterns = [
    path('',views.index, name='kiosk'),
    path('cusorder/', views.cusorder, name='cusorder'),
]
