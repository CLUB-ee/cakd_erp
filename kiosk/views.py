
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


def index(request):
    return render(request, "kiosk/kiosk.html")


def cusorder(request):

    if request.method == "POST":

        menuid = request.POST.get('menuid')
        cusord = Cusord(menu_id=Menu.objects.get(menu_id=menuid))
        cusord.save()

    return render(request, 'kiosk/kiosk.html', messages.info(request, "주문이 완료 되었습니다."))
