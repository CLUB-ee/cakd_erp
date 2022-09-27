from django.shortcuts import render, redirect
from rest_framework.response import Response
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Cusord, Instock, Manager, Material, Menu, Ord, Outstock, Recipe
from .serializers import CusordSerializer, InstockSerializer, ManagerSerializer,\
    MaterialSerializer, MenuSerializer, OrdSerializer, OutstockSerializer, RecipeSerializer
from rest_framework import generics
from rest_framework import viewsets


class CusordViewset(viewsets.ModelViewSet):
    queryset = Cusord.objects.all()
    serializer_class = CusordSerializer


class InstockList(viewsets.ModelViewSet):
    queryset = Instock.objects.all()
    serializer_class = InstockSerializer


class ManagerList(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class MaterialList(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MenuList(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class OrdList(viewsets.ModelViewSet):
    queryset = Ord.objects.all()
    serializer_class = OrdSerializer


class OutstockList(viewsets.ModelViewSet):
    queryset = Outstock.objects.all()
    serializer_class = OutstockSerializer


class RecipeList(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
