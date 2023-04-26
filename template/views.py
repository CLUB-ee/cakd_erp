
import numpy as np
from django.db.models import Count, Sum
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from datetime import datetime
from bisect import insort
from gc import get_objects
from pipes import Template
from sqlite3 import Cursor
# from termios import TIOCPKT_FLUSHREAD
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
from datetime import datetime, date
from django.core.exceptions import ObjectDoesNotExist
from collections import Counter
import joblib
import pandas as pd
import pickle

from django.core.exceptions import ObjectDoesNotExist
from sklearn.linear_model import ElasticNet


def stock(request):
    return render(request, 'stock.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


"""코드 개선"""
# from .models import Material, Menu, Cusord
# from .utils import ML


def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def dash(request):
    from django.db.models import Sum, Count, F
    from django.db.models.functions import TruncMonth
    from datetime import datetime, timedelta
    from dateutil.relativedelta import relativedelta

    material = Material.objects.all()
    today = datetime.now().date()

    if request.method == 'POST':
        month_day = request.POST.get('month')
        if not validate_date(month_day):
            month_day = today.isoformat()
    else:
        month_day = today.isoformat()

    # 일매출
    daily_menu_orders = Cusord.objects.filter(out_time=month_day).values(
        'menu_id').annotate(order_count=Count('menu_id'))
    daily_menu_sales = {
        menu_order['menu_id']: menu_order['order_count'] for menu_order in daily_menu_orders}
    # 일매출 총합
    daily_sales = sum(menu.menu_pri * daily_menu_sales.get(menu.menu_id, 0)
                      for menu in Menu.objects.all())
    daily_sales = f"{daily_sales:,} 원"
    # 월매출
    monthly_menu_orders = Cusord.objects.filter(out_time__startswith=month_day[:7]).values(
        'menu_id').annotate(order_count=Count('menu_id'))
    monthly_menu_sales = {
        menu_order['menu_id']: menu_order['order_count'] for menu_order in monthly_menu_orders}
    # 월 매출 총합
    monthly_sales = sum(menu.menu_pri * monthly_menu_sales.get(menu.menu_id, 0)
                        for menu in Menu.objects.all())
    monthly_sales = f"{monthly_sales:,} 원"

    # 일 메뉴별 판매량
    menu_sales_By_day = [(menu, menu_orders['order_count']) for menu in Menu.objects.all(
    ) for menu_orders in daily_menu_orders if menu_orders['menu_id'] == menu.menu_id]

    # 직전 12개월 월별 매출량
    # 12개월 전부터 해당 월 매출까지 집계
    # total_sales = []
    # start_date = datetime.now() - timedelta(days=30*12)
    # # end_date = datetime.now()
    # for i in range(12):
    #     current_month_start = start_date.replace(
    #         month=(start_date.month + i) % 12 + 1)
    #     current_month_end = current_month_start.replace(
    #         month=(start_date.month + i) % 12 + 1, day=1) - timedelta(days=1)

    #     monthly_order_count = Cusord.objects.filter(out_time__range=(current_month_start, current_month_end)).\
    #         values('menu_id').annotate(order_count=Count('menu_id'))
    #     monthly_order_count_dict = {
    #         menu_order['menu_id']: menu_order['order_count'] for menu_order in monthly_order_count}

    #     # 월 매출 총합
    #     monthly_sales = sum(menu.menu_pri * monthly_order_count_dict.get(menu.menu_id, 0)
    #                         for menu in Menu.objects.all())
    #     total_sales.append((start_date, monthly_sales))

    # 월 단위로 그룹화하여 통계 처리 예시
    # statistics_sales = sum(menu.menu_pri * monthly_menu_sales_.get(menu.menu_id, 0) for menu in Menu.objects.all())
    # statistics_cnt = monthly_menu_orders_.annotate(month=TruncMonth('out_time')).values('month').annotate(total=Count('menu_id')).order_by('month')
    # total_sales = []
    # start_date = datetime.now() - timedelta(days=30*12)
    # for i in range(12):
    #     # 월별로 start_date와 end_date를 각각 복사하여 새로운 변수에 저장
    #     current_month = (start_date.month + i - 1) % 12 + 1
    #     current_year = start_date.year + ((start_date.month + i - 1) // 12)
    #     current_month_start = datetime(current_year, current_month, 1)
    #     current_month_end = (current_month_start + relativedelta(day=31)
    #                          ).replace(hour=23, minute=59, second=59)

    #     monthly_order_count = Cusord.objects.filter(out_time__range=(current_month_start, current_month_end)).\
    #         values('menu_id').annotate(order_count=Count('menu_id'))
    #     monthly_order_count_dict = {
    #         menu_order['menu_id']: menu_order['order_count'] for menu_order in monthly_order_count}

    #     # 월 매출 총합
    #     monthly_sales = sum(menu.menu_pri * monthly_order_count_dict.get(menu.menu_id, 0)
    #                         for menu in Menu.objects.all())
    #     total_sales.append((current_month_start, monthly_sales))
    from datetime import datetime, timedelta
    import calendar
    from django.db.models import Count
    # from myapp.models import Cusord, Menu

    total_sales = []
    start_date = datetime.now() - timedelta(days=30*12)
    for i in range(12):
        # 월별로 start_date와 end_date를 각각 복사하여 새로운 변수에 저장
        current_month = (start_date.month + i - 1) % 12 + 1
        current_year = start_date.year + ((start_date.month + i - 1) // 12)
        current_month_start = datetime(current_year, current_month, 1)
        current_month_end = datetime(current_year, current_month, calendar.monthrange(
            current_year, current_month)[1])

        # 월별 주문 수량을 메뉴별로 집계
        monthly_order_count = Cusord.objects.filter(out_time__range=(current_month_start, current_month_end)).\
            values('menu_id').annotate(order_count=Count('menu_id'))
        monthly_order_count_dict = {
            menu_order['menu_id']: menu_order['order_count'] for menu_order in monthly_order_count}
        menu_ids = monthly_order_count.values_list('menu_id', flat=True)

        # 월 매출 총합
        menu_dict = {
            menu.menu_id: menu for menu in Menu.objects.filter(menu_id__in=menu_ids)}
        monthly_sales = sum(menu_dict[menu_id].menu_pri * monthly_order_count_dict.get(menu_id, 0)
                            for menu_id in menu_ids)

        total_sales.append(
            (current_month_start.isoformat()[:7], monthly_sales))

    # 예측 판매량
    menu_cnt_pred, _ = ML()

    return render(request, 'dash.html', {'material': material, 'menu_sales_By_day': menu_sales_By_day, 'total_sales': total_sales,
                                         'menu_cnt_pred': menu_cnt_pred, 'daily_sales': daily_sales, 'monthly_sales': monthly_sales})


    # return render(request, 'dash.html', {'material': material, 'sale_total': sales_total,\
    #     'menu_cnt_pred': menu_cnt_pred,'daily_sales':daily_sales,'monthly_sales':monthly_sales})
"""개선 전 코드"""

# def validate_date(date_text):
# 	try:
# 		datetime.strptime(date_text,"%Y-%m-%d")
# 		return True
# 	except ValueError:
# 		print("Incorrect data format({0}), should be YYYY-MM-DD".format(date_text))
# 		return False

# def dash(request):

#     material = Material.objects.all()
#     if request.method == 'POST':
#         if validate_date(request.POST.get('month')):# 특정 날짜를 누르면 실행
#             month_day = request.POST.get('month')
#         else: # 단순히 확인버튼만 누르면 오늘날짜로 출력
#             month_day = date.today().isoformat()
#     else: # 사이트 새로고침시 오늘날짜로 동일하게 매출 출력
#     month_day = date.today().isoformat() # 오늘 날짜의 YYYY-MM-DD 형태

# menu_li_day = Cusord.objects.filter(out_time=month_day)
# menu_day = [str(i.menu_id.menu_id) for i in list(menu_li_day)]
# menu_day = Counter(menu_day)
# menu_list = []
# for i in [str(j) for j in range(1, 6)]:
#     menu_list.append(menu_day[i])

# menu_name_list = []
# for i in range(1, 6):
#     menu_name_list.append(Menu.objects.get(menu_id=i))
# sales_total = zip(menu_name_list, menu_list)

#     # 일매출
#     daily_sales = 0
#     for i,j in enumerate([str(j) for j in range(1,6)]):
#         daily_sales += (menu_day[j] * Menu.objects.get(pk=i+1).menu_pri)
#     daily_sales = str(daily_sales)+' 원'
#     # 월매출
#     month = month_day[:7]
#     menu_li_month = Cusord.objects.filter(out_time__startswith=month)
#     menu_month = [str(i.menu_id.menu_id) for i in list(menu_li_month)]
#     menu_month = Counter(menu_month)
#     monthly_sales = 0
#     for i,j in enumerate([str(j) for j in range(1,6)]):
#         monthly_sales += (menu_month[j] * Menu.objects.get(pk=i+1).menu_pri)
#     monthly_sales = str(monthly_sales)+' 원'

#     menu_cnt_pred,_= ML()

#     return render(request, 'dash.html', {'material': material, 'sale_total': sales_total,\
#         'menu_cnt_pred': menu_cnt_pred,'daily_sales':daily_sales,'monthly_sales':monthly_sales})


# 머신러닝
def ML():
    elastic = joblib.load('template/elastic_model.pkl')
    df = pd.DataFrame(columns=['menuId', 'APM', 'weekday'])
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

    menu_cnt_pred = zip(menu_name_li, sum_list)
    return menu_cnt_pred, sum_list


class MyAPIView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'my.html'

    def get(self, request):
        queryset = Manager.objects.get(pk=1)
        return Response({'man': queryset})

# 발주현황 보기


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
        return classmodel.objects.get(menu_id=id_1, mate_id=id_2).mate_usage
    except classmodel.DoesNotExist:
        return 0


# 발주신청


class OrdappAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'orderapp.html'

    def get(self, request, **kwargs):
        mate_list = Material.objects.all().order_by('mate_id')
        _, sum_list = ML()

        # 메뉴 1부터 5, 재료 1부터 11의 레시피 가져오기
        recipe_list_sum = np.zeros(11)
        for menu in range(1, 6):
            recipe_list = np.array(
                [get_or_none(Recipe, menu, mat) * sum_list[menu - 1] for mat in range(1, 12)])
            recipe_list_sum += recipe_list

        # 매니저의 마진율 적용
        margin = Manager.objects.get(pk=1).man_safe
        recipe_list_sum = np.ceil(recipe_list_sum * margin).astype(int)

        mate_recipe_list = zip(mate_list, recipe_list_sum)
        return Response({'mate_list': mate_list, 'mate_recipe_list': mate_recipe_list})


# 발주신청 함수
def createform(request):
    if request.method == 'POST':
        Ord.objects.create()
        mateid_list = request.POST.getlist('mateid', [])
        mateid_list = list(map(int, mateid_list))
        mate_quan_list = request.POST.getlist('mate_quan', [])
        mate_quan_list = [int(q) if q else 0 for q in mate_quan_list]

        for i in range(len(mateid_list)):
            instock = Instock()
            instock.ord_num = Ord.objects.latest('ord_num')
            if i < len(mateid_list):
                instock.mate_id = Material.objects.get(mate_id=mateid_list[i])
            if i < len(mate_quan_list):
                instock.in_quan = mate_quan_list[i]
            instock.save()

    return render(request, 'orderapp.html', messages.info(request, "발주가 완료 되었습니다."))


# 매출
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
