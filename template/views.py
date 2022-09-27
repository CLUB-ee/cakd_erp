
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
from django.db.models import Max, Min, Avg, Sum, Count
import pandas as pd
import json
from django.http import JsonResponse
from django.contrib import messages
import joblib
import pandas as pd
import pickle
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from collections import Counter
import joblib
import pandas as pd
import pickle
from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from sklearn.linear_model import ElasticNet


def stock(request):
    return render(request, 'stock.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')

# dash input 함수


def index(request):
    return render(request, "dash.html")


def dash(request):

    queryset1 = Material.objects.all()
    if request.method == 'POST':
        month = request.POST.get('month')
        menu_li = Cusord.objects.filter(out_time=month)
        menu_ = [str(i.menu_id.menu_id) for i in list(menu_li)]

    from collections import Counter

    menu_ = Counter(menu_)
    menu_list = []
    for i in [str(j) for j in range(1, 6)]:
        menu_list.append(menu_[i])

    menu_name_list = []
    for i in range(1, 6):
        menu_name_list.append(Menu.objects.get(menu_id=i))

    menu_zip = zip(menu_name_list, menu_list)

    elastic = joblib.load('template/elastic_model.pkl')
    df = pd.DataFrame(columns=['menuId', 'APM', 'weekday'])
    global sum_list
    sum_list = []
    menu_name_li = []
    next_day = datetime.now().weekday() + 1
    for i in range(1, 6):
        data = [i, 0, next_day]
        data_2 = [i, 1, next_day]
        df.loc[0, :] = data
        df.loc[1, :] = data_2
        y_pred = elastic.predict(df)
        predict = round(sum(y_pred))
        sum_list.append(predict)
        menu_name_li.append(Menu.objects.get(pk=i).menu_name)

    zip_list = zip(menu_name_li, sum_list)

    return render(request, 'dash.html', {'material': queryset1, 'sale_total': menu_zip, 'zip': zip_list})


class MyAPIView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'my.html'

    def get(self, request):
        queryset = Manager.objects.get(pk=1)
        return Response({'man': queryset})

# 발주현황 instock


class OrderAPIView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'orders.html'

    def get(self, request):

        cnt = Instock.objects.count()
        for i in range(1, cnt+1):
            total = (Instock.objects.get(pk=i).in_quan) * \
                (Instock.objects.get(pk=i).mate_id.unit_cost)/10
            Instock.objects.filter(pk=i).update(in_total=total)

        queryset = Instock.objects.all().order_by(('-ord_num'))

        return Response({'instock': queryset})


def get_or_none(classmodel, id_1, id_2):
    try:
        return classmodel.objects.filter(menu_id=id_1).get(mate_id=id_2).mate_usage
    except classmodel.DoesNotExist:
        return 0


class OrdappAPIView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'orderapp.html'

    # serializer_class = ManagerSerializer
    def get(self, request, **kwargs):
        cnt = Instock.objects.count()
        for i in range(1, cnt+1):
            total = Instock.objects.get(
                pk=i).in_quan * (Instock.objects.get(pk=i).mate_id.unit_cost)/10
            Instock.objects.filter(pk=i).update(in_total=total)
        queryset = Instock.objects.all().order_by('-in_num')
        mate_list = Material.objects.all().order_by('mate_id')
        global sum_list
        sum_list = sum_list

        # 소불고기 1 제육 2 비빔밥 3 떡갈비 4 보쌈 5
        # 레시피 가져오기
        import numpy as np
        import math
        recipe_list_sum = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        # 메뉴 1부터 5
        for menu in range(5):
            # 재료 1부터 11
            recipe_list = np.array([])
            for mat in range(1, 12):
                intance = get_or_none(Recipe, menu+1, mat) * sum_list[menu]
                recipe_list = np.append(recipe_list, np.array([intance]))
            recipe_list_sum = recipe_list_sum + recipe_list

        # 매니저의 마진율
        margin = Manager.objects.get(pk=1).man_safe
        recipe_list_sum = list(
            map(lambda x: math.ceil(x*margin), recipe_list_sum))
        mate_recipe_list = zip(mate_list, recipe_list_sum)
        return Response({'mate_list': mate_list,
                        'mate_recipe_list': mate_recipe_list})


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
