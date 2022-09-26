
from gc import get_objects
from pipes import Template
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# 클래스 기반의 Rest CRUD 처리
from erp.models import Cusord, Instock, Manager, Material, Menu, Ord, Outstock, Recipe
from erp.serializers import CusordSerializer, InstockSerializer, OutstockSerializer, ManagerSerializer

from rest_framework import status
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

# Create your views here.


def index(request):
    return render(request, "kiosk/kiosk.html")


def cusorder(request):

    if request.method == "POST":

        menuid = request.POST.get('menuid')
        cusord = Cusord(menu_id=Menu.objects.get(menu_id=menuid))
        cusord.save()

    return render(request, 'kiosk/kiosk.html', messages.info(request, "주문이 완료 되었습니다."))


# class CusordAPIView(APIView):

#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'orders.html'

#     # serializer_class = ManagerSerializer

#     def get(self, request):
#         # if Instock.objects.exists():
#         cnt = Cusord.objects.count()
#         for i in range(1,cnt+1):
#             total = (Cusord.objects.get(pk=i).in_quan) * (Cusord.objects.get(pk=i).mate_id.unit_cost)
#             Cusord.objects.filter(pk=i).update(in_total=total)

#         queryset = Cusord.objects.all().order_by('-in_num')

#         return Response({'cusord': queryset})
