
from bisect import insort
from gc import get_objects
from pipes import Template
from sqlite3 import Cursor
from termios import TIOCPKT_FLUSHREAD
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from erp.models import Cusord, Instock, Manager, Material, Menu, Ord, Outstock, Recipe
from erp.serializers import CusordSerializer, InstockSerializer, OutstockSerializer, ManagerSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from django.db.models import Max, Min, Avg, Sum
import pandas as pd
import json
from django.http import JsonResponse
from django.contrib import messages
import joblib
import pandas as pd
import pickle
from datetime import datetime

from erp.views import test
from django.core.exceptions import ObjectDoesNotExist

<<<<<<< Updated upstream
# def dash(request):
#     context = {
#         'menu' : Menu.objects.all(),
#         'material' : Material.objects.all()
#     }
#     return render(request, 'dash.html', context)



def stock(request):
    return render(request, 'stock.html')

=======
>>>>>>> Stashed changes

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
        for i in range(1, cnt+1):
            total = (Instock.objects.get(pk=i).in_quan) * \
                (Instock.objects.get(pk=i).mate_id.unit_cost)
            Instock.objects.filter(pk=i).update(in_total=total)
        
        queryset = Instock.objects.all().order_by(('-ord_num'))
        
        return Response({'instock': queryset})
        
=======
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
def get_or_none(classmodel,id_1,id_2):
    try: 
        return classmodel.objects.filter(menu_id=id_1).get(mate_id=id_2).mate_usage
    except classmodel.DoesNotExist:
        return 0
=======

>>>>>>> Stashed changes

class OrdappAPIView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'orderapp.html'

    # serializer_class = ManagerSerializer
<<<<<<< Updated upstream
    
 
    def get(self, request,**kwargs):
        
=======

    def get(self, request, **kwargs):
>>>>>>> Stashed changes
        cnt = Instock.objects.count()

        for i in range(1, cnt+1):
            total = Instock.objects.get(
                pk=i).in_quan * Instock.objects.get(pk=i).mate_id.unit_cost
            Instock.objects.filter(pk=i).update(in_total=total)
        queryset = Instock.objects.all().order_by('-in_num')
<<<<<<< Updated upstream
        
        mate_list = Material.objects.all().order_by('mate_id')

        global sum_list

        # 소불고기 1 제육 2 비빔밥 3 떡갈비 4 보쌈 5
        # 레시피 가져오기 
        import numpy as np
        recipe_list_sum = np.array([0,0,0,0,0,0,0,0,0,0,0])
        # 메뉴 1부터 5
        for menu in range(5):
            for mat in range(1,12):
                recipe_list = np.array([])
                intance = get_or_none(Recipe,menu,mat) * sum_list[menu]
                recipe_list = np.append(recipe_list, np.array([intance]))
            recipe_list_sum =  recipe_list_sum + recipe_list
        
        mate_recipe_list = zip(mate_list,recipe_list_sum)
        return Response({'ord_stock': queryset,'mate_list':mate_list,'recipe_list':recipe_list,'mate_recipe_list':mate_recipe_list})
=======

        mate_list = Material.objects.all().order_by('-mate_id')

        minOrderValue = {'무': 5, '마늘': 3}

        return Response({'ord_stock': queryset, 'mate_list': mate_list, 'minOrderValue': minOrderValue})
>>>>>>> Stashed changes

# 발주 신청 폼


def createform(request):
    if request.method == 'POST':
        Ord.objects.create()
        mateid_list = request.POST.getlist('mateid')
        mateid_list = list(map(int, mateid_list))
        mate_quan_list = request.POST.getlist('mate_quan')
        mate_quan_list = list(map(int, mate_quan_list))

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

   

<<<<<<< Updated upstream
=======
#         month = request.POST.get('month')

#         month_ = Cusord(out_time=Cusord.objects.filter(out_time.month == datetime.strptime(month, '%m')))

#     return redirect(request, 'template/dash.html', {'month':month_})


# class DashAPIView(APIView):

#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'dash.html'
#     # serializer_class = ManagerSerializer

#     def month(request):
>>>>>>> Stashed changes


class DashAPIView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dash.html'
    # serializer_class = ManagerSerializer

<<<<<<< Updated upstream
    def get(self, request):
        queryset = Menu.objects.all()
        queryset1 = Material.objects.all()
        
        # 머신러닝 (내일 메뉴 예상 판매량 확인)
        elastic = joblib.load('template/elastic_model.pkl')
        df = pd.DataFrame(columns=['menuId', 'APM', 'weekday'])   
        global sum_list
        sum_list=[]
        menu_name_li =[]
        next_day = datetime.now().weekday() + 1
        for i in range(1,6):
            data = [i,0,next_day]
            data_2 = [i,1,next_day]
            df.loc[0,:] = data
            df.loc[1,:] = data_2
            y_pred = elastic.predict(df)
            predict = round(sum(y_pred),1)
            sum_list.append(predict)
            menu_name_li.append(Menu.objects.get(pk=i).menu_name)
        
        zip_list=zip(menu_name_li,sum_list)
        # [2,2,2,2,2]
        
        
        

        return Response({'menu': queryset, 'material':queryset1,'zip':zip_list})
    
=======
#             menu_sum = Menu(menu_sum = Menu.objects.filter(menu_id = menu_))

#         return Response({'menu_sum': menu_sum})


#     def get(self, request):
#         queryset = Menu.objects.all()
#         queryset1 = Material.objects.all()


#         time_list=[]
#         for i in Cusord.objects.all():

#             time = i.out_time
#             time = datetime.strftime(time,'%m-%d')
#             time_list.append(time)


#         return Response({'menu': queryset, 'material':queryset1, 'time': set(time_list)})

# dash input 함수

def index(request):
    return render(request, "dash.html")


def dash(request):
    menu_name = Menu.objects.all()
    queryset1 = Material.objects.all()
    if request.method == 'POST':
        month = request.POST.get('month')
        menu_li = Cusord.objects.filter(out_time=month)
        menu_ = [str(i.menu_id.menu_id) for i in list(menu_li)]

    menu_list = []

    for i in menu_:
        total = Menu.objects.get(menu_id=i)
        menu_list.append(total)

    # menu_dic = Counter(menu_list)
    # menu_list = json.dumps(menu_dic)
    queryset = Menu.objects.all()

    return render(request, 'dash.html', {'menu': queryset, 'menu_n': menu_name, 'material': queryset1, 'sale_total': menu_list})

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
        sum_list = []
        next_day = datetime.now().weekday() + 1
        for i in range(1, 6):
            data = [i, 0, next_day]
            data_2 = [i, 1, next_day]
            df.loc[0, :] = data
            df.loc[1, :] = data_2
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

        return Response({'menu': queryset, 'material': queryset1, 'predict': predict})

>>>>>>> Stashed changes

class SaleAPIView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'sale.html'
    # serializer_class = ManagerSerializer

    def get(self, request):
        # 각 메뉴 수량 * 메뉴가격
        for i in range(1, Menu.objects.count()+1):
            total = (Menu.objects.get(pk=i).menu_pri) * \
                (Menu.objects.get(pk=i).menu_cnt)
            Menu.objects.filter(pk=i).update(menu_sum=total)
        queryset = Menu.objects.all()
        sale_total = Menu.objects.aggregate(Sum('menu_sum'))
        return Response({'menu': queryset, 'sale_total': sale_total})

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
