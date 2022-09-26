
from gc import get_objects
from pipes import Template
from urllib import request
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
from django.db.models import Q
from django.db.models import Max, Min, Avg, Sum  # 뷰에서 db 계산할때 해야함
import pandas as pd
import json
from django.http import JsonResponse

def dash(request):
    context = {
        'menu' : Menu.objects.all(),
        'material' : Material.objects.all()
    }
    return render(request, 'dash.html', context)



def stock(request):
    return render(request, 'stock.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')

class MyAPIView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'my.html'
    # serializer_class = ManagerSerializer

    def get(self, request):
        queryset = Manager.objects.get(pk=1)
        return Response({'man': queryset})

# 발주현황 instock
class OrderAPIView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'orders.html'
 
    # serializer_class = ManagerSerializer

    def get(self, request):
        # if Instock.objects.exists():
        cnt = Instock.objects.count()
        for i in range(1,cnt+1):
            total = (Instock.objects.get(pk=i).in_quan) * (Instock.objects.get(pk=i).mate_id.unit_cost)
            Instock.objects.filter(pk=i).update(in_total=total)
        
        queryset = Instock.objects.all().order_by('-in_num')
        
        return Response({'instock': queryset})
      

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     quan = Instock.objects.all().in_quan
    #     print(quan)
    #     cost = Instock.objects.all().mate_id.unit_cost
    #     context['total'] = quan * cost
    #     context['q'] = Instock.objects.all()
    #     zip_context = zip(context['total'],context['q'])
    #     return zip_context
# 발주신청
class OrdappAPIView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'orderapp.html'
 
    # serializer_class = ManagerSerializer
 
    def get(self, request,**kwargs):
        cnt = Instock.objects.count()
    
        for i in range(1,cnt+1):
            total = Instock.objects.get(pk=i).in_quan * Instock.objects.get(pk=i).mate_id.unit_cost
            Instock.objects.filter(pk=i).update(in_total=total)
        queryset = Instock.objects.all().order_by('-in_num')
        
        stock = Material.objects.all().order_by('-mate_id')

        minOrderValue = {'무':5,'마늘':3}

        return Response({'ord_stock': queryset,'stock':stock,'minOrderValue':minOrderValue})

# 발주 신청 폼
def createform(request):
    if request.method == 'POST':
        instock = Instock()
        ord = Ord()
        ord.objects.create()
        ord.save()
        # instock.mate_id = 10
        instock.in_quan = request.POST('mate_quan[0]')
        instock.save()
    return redirect('orderapp')
# def create(self,request,**kwargs):
    #     in_quan_1 = kwargs.get('mate_3')
    #     in_quan_2 = kwargs.get('mate_7')
    #     in_quan_3 = kwargs.get('mate_4')
 
    #     Instock.objects.bulk_create([
    #         Instock(name="God",ord_num=1,mate_id=,in_quan=in_quan_1),
    #         Instock(name="Demi God",mate_id=),
    #         Instock(name="Mortal",in_quan=)
    #         ])

   



# class DashAPIView(APIView):

#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'dash.html'
#     # serializer_class = ManagerSerializer

#     def get(self, request):
#         li = []
#         for i in range(1, Menu.objects.count()+1):
#             name = Menu.objects.get(pk=i).menu_name
#             li.append(name)

#         return Response({'menu': li})

class SaleAPIView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'sale.html'
    # serializer_class = ManagerSerializer

    def get(self, request):
        # 각 메뉴 수량 * 메뉴가격
        for i in range(1,Menu.objects.count()+1):
            total = (Menu.objects.get(pk=i).menu_pri) * (Menu.objects.get(pk=i).menu_cnt)
            Menu.objects.filter(pk=i).update(menu_sum = total)
        queryset = Menu.objects.all()
        sale_total = Menu.objects.aggregate(Sum('menu_sum'))
        return Response({'menu': queryset,'sale_total':sale_total})
    
    

        
    # def get(self, request):
    #     queryset = Material.objects.all()
    #     return Response({'mate': queryset})
    # def get_queryset(self):
    #     q = self.kwargs['q']
    #     post_list = Menu.objects.filter(
    #     Q(title__contains=q) | Q(tags__name__contains=q)
    # ).distinct()
    #        ÷     xz return post_list

    # def get_context_data(self, **kwargs):
    #     context = super(PostSearch, self).get_context_data()
    #     q = self.kwargs['q']
    #     context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'
    #     return context





# Create your views here.
