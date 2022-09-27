from dataclasses import field
from rest_framework import serializers
from erp.models import Cusord, Instock, Manager, Material, Menu, Ord, Outstock, Recipe
from drf_queryfields import QueryFieldsMixin
# Menu Serializer


class MenuSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

# Material Serializer


class MaterialSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

# Ord Serializer


class OrdSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Ord
        fields = '__all__'

# CusOrd Serializer


class CusordSerializer(serializers.ModelSerializer):
    menu_id = MenuSerializer(read_only=True)

    class Meta:
        model = Cusord
        fields = '__all__'

# InStock Serializer


class InstockSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    mate_id = MaterialSerializer(read_only=True)

    class Meta:
        model = Instock
        fields = '__all__'

# Outstock Serializer


class OutstockSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    mate_id = MaterialSerializer(read_only=True)
    cus_ord_num = CusordSerializer(read_only=True)

    class Meta:
        model = Outstock
        fields = '__all__'

# Recipe Serializer


class RecipeSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    mate_id = MaterialSerializer(read_only=True)
    menu_id = MenuSerializer(read_only=True)

    class Meta:
        model = Recipe
        fields = '__all__'

# Manager Serializer


class ManagerSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'
