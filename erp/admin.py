# from ast import In
from django.contrib import admin
from .models import Cusord, Instock, Manager, Material, Menu, Ord, Outstock, Recipe
# Register your models here.

admin.site.register(Cusord)
admin.site.register(Instock)
admin.site.register(Manager)
admin.site.register(Material)
admin.site.register(Menu)
admin.site.register(Ord)
admin.site.register(Outstock)
admin.site.register(Recipe)
