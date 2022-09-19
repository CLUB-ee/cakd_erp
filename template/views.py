
from pipes import Template
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# 클래스 기반의 Rest CRUD 처리
from erp.models import Cusord, Instock, Manager, Material, Menu, Ord, Outstock, Recipe
from erp.serializers import CusordSerializer, InstockSerializer, OutstockSerializer, ManagerSerializer

from rest_framework import generics
from rest_framework import viewsets
# generics 에 목록과 생성 API가 정의되어 있음
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response


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


class OrderAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'my.html'
    serializer_class = ManagerSerializer

    # def get(self, menu_id):
    #     menu = get_object_or_404(Menu, menu_id=menu_id)
    #     content = {'menu': menu.menu_id}
    # return Response(content)
    def get(self, request):
        queryset = Manager.objects.get(man_id=1)
        return Response({'man': queryset})

# Create your views here.
