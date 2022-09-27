
from bisect import insort
from email.feedparser import BytesFeedParser
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
from django.contrib import messages
import joblib
import pandas as pd
import pickle
from datetime import datetime

# def dash(request):
#     context = {
#         'menu' : Menu.objects.all(),
#         'material' : Material.objects.all()
#     }
#     return render(request, 'dash.html', context)



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
       
        cnt = Instock.objects.count()
        for i in range(1,cnt+1):
            total = (Instock.objects.get(pk=i).in_quan) * (Instock.objects.get(pk=i).mate_id.unit_cost)
            Instock.objects.filter(pk=i).update(in_total=total)
        
        queryset = Instock.objects.all().order_by(('-ord_num'))
        
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
        
        mate_list = Material.objects.all().order_by('-mate_id')

        minOrderValue = {'무':5,'마늘':3}

        return Response({'ord_stock': queryset,'mate_list':mate_list,'minOrderValue':minOrderValue})

# 발주 신청 폼
def createform(request):
    if request.method == 'POST':
        Ord.objects.create()
        mateid_list = request.POST.getlist('mateid')
        mateid_list = list(map(int,mateid_list))
        mate_quan_list = request.POST.getlist('mate_quan')
        mate_quan_list = list(map(int,mate_quan_list))
        
        for i in range(11):
            instock = Instock()
            instock.ord_num = Ord.objects.latest('ord_num')
            instock.mate_id = Material.objects.get(mate_id=mateid_list[i])
            instock.in_quan = mate_quan_list[i]
            instock.save()
     
            
    return render(request, 'orderapp.html', messages.info(request, "발주가 완료 되었습니다."))
    

# def cusorder(request):
    
#     if request.method == "POST":

#         menuid= request.POST.get('menuid')
#         cusord = Cusord(menu_id=Menu.objects.get(menu_id=menuid) )            
#         cusord.save()




#         return render(request, "kiosk/cusorder.html",{'lis':cusord})
# def create(self,request,**kwargs):
    #     in_quan_1 = kwargs.get('mate_3')
    #     in_quan_2 = kwargs.get('mate_7')
    #     in_quan_3 = kwargs.get('mate_4')
 
    #     Instock.objects.bulk_create([
    #         Instock(name="God",ord_num=1,mate_id=,in_quan=in_quan_1),
    #         Instock(name="Demi God",mate_id=),
    #         Instock(name="Mortal",in_quan=)
    #         ])

   



class DashAPIView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dash.html'
    # serializer_class = ManagerSerializer

    def get(self, request):
        queryset = Menu.objects.all()
        queryset1 = Material.objects.all()
        
        # 머신러닝 (내일 메뉴 예상 판매량 확인)
        elastic = joblib.load('template/elastic_model.pkl')
        df = pd.DataFrame(columns=['menuId', 'APM', 'weekday'])
        # 소불고기 1
        # 제육 2
        # 비빔밥 3
        # 떡갈비 4
        # 보쌈 5
        sum_list=[]
        next_day = datetime.now().weekday() + 1
        for i in range(1,6):
            data = [i,0,next_day]
            data_2 = [i,1,next_day]
            df.loc[0,:] = data
            df.loc[1,:] = data_2
            y_pred = elastic.predict(df)
            predict = sum(y_pred)
            sum_list.append(predict)
        # [2,2,2,2,2]
        # 1	소고기
        # 2	돼지고기
        # 3	양파
        # 4	파
        # 5	바섯
        # 6	당근
        # 7	마늘
        # 8	청양고추
        # 9	애호박
        # 10	계란
        # 11	무

        # 레시피 가져오기
        beef = Recipe.objects.all()
        # pork
        

        return Response({'menu': queryset, 'material':queryset1,'predict':predict})
    

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
