from django.shortcuts import render, redirect
from rest_framework.response import Response
# from django.http import JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# 클래스 기반의 Rest CRUD 처리
from .models import Cusord, Instock, Manager, Material, Menu, Ord, Outstock, Recipe
from .serializers import CusordSerializer, InstockSerializer, ManagerSerializer, MaterialSerializer, MenuSerializer, OrdSerializer, OutstockSerializer, RecipeSerializer
from rest_framework import generics
from rest_framework import viewsets


def test(request):
    cusord = Cusord.objects
    return render(request, 'erp/test.html', {'test': cusord})

# get json


def get_json(arr):
    if arr:
        return arr[0]
    return arr

# time parsing


def time_str(timestamp):
    timestamp = timestamp.strftime("%Y.%m.%d. %H:%M:%S")
    return timestamp

# generics 에 목록과 생성 API가 정의되어 있음


class CusordViewset(viewsets.ModelViewSet):
    queryset = Cusord.objects.all()
    serializer_class = CusordSerializer
    # response = Response(serializer_class.data)
    # print(response)


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


# class InstockList(generics.ListCreateAPIView):
#     queryset = Instock.objects.all()
#     serializer_class = InstockSerializer


# class OutstockList(generics.ListCreateAPIView):
#     queryset = Outstock.objects.all()
#     serializer_class = OutstockSerializer

# from django.shortcuts import get_object_or_404
# # from .models import Post, Category, Tag, Comment
# # from .forms import CommentForm
# from django.core.exceptions import PermissionDenied
# from django.utils.text import slugify
# from django.db.models import Q


# # Create your views here.
# class PostList(ListView):
#     model = Post
#     ordering = '-pk'
#     paginate_by = 30

#     def get_context_data(self, **kwargs):
#         context = super(PostList, self).get_context_data()
#         context['categories'] = Category.objects.all()
#         context['no_category_post_count'] = Post.objects.filter(
#             category=None).count()
#         return context


# class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
#     model = Post
#     fields = ['title', 'hook_text', 'content',
#               'head_image', 'file_upload', 'category']

#     def test_func(self):
#         return self.request.user.is_superuser or self.request.user.is_staff

#     def form_valid(self, form):
#         current_user = self.request.user
#         if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
#             form.instance.author = current_user

#             response = super(PostCreate, self).form_valid(form)

#             tags_str = self.request.POST.get('tags_str')
#             if tags_str:
#                 tags_str = tags_str.strip()
#                 tags_str = tags_str.replace(',', ';')
#                 tags_list = tags_str.split(';')
#                 for t in tags_list:
#                     t = t.strip()
#                     tag, is_tag_created = Tag.objects.get_or_create(name=t)
#                     if is_tag_created:
#                         tag.slug = slugify(t, allow_unicode=True)
#                         tag.save()
#                     self.object.tags.add(tag)
#             return response
#         else:
#             return redirect('/blog/')
