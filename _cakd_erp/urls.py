"""_cakd_erp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from importlib.resources import path
from django.urls import include, path, re_path
from django.contrib import admin
from erp import views
from rest_framework import routers
from django.urls import path

router = routers.DefaultRouter()
router.register(r'api_cusord', views.CusordViewset)
router.register(r'api_instock', views.InstockList)
router.register(r'api_manager', views.ManagerList)
router.register(r'api_material', views.MaterialList)
router.register(r'api_menu', views.MenuList)
router.register(r'api_Ord', views.OrdList)
router.register(r'api_outstock', views.OutstockList)
router.register(r'api_recipe', views.RecipeList)

# urlpatterns = [
#     url(r'^', include(router.urls)),
#     url(r'^admin/', admin.site.urls),
#     path('tmep/', include('template.urls')),
#     path('kiosk/', include('kiosk.urls')),
# ]


urlpatterns = [
    path('rest/', include(router.urls)),
    re_path(r'^admin/', admin.site.urls),
    path('tmep/', include('template.urls')),
    path('', include('kiosk.urls')),
]
