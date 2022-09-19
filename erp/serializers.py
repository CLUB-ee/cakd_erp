from dataclasses import field
from rest_framework import serializers
from erp.models import Cusord, Instock, Manager, Material, Menu, Ord, Outstock, Recipe
from drf_queryfields import QueryFieldsMixin


# Menu Serializer
class MenuSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

    # 신규 instance를 생성해서 리턴해준다
    def create(self, validated_data):
        return Menu.objects.create(**validated_data)

    # 생성되어 있는 instance 를 저장한 후 리턴해준다
    def update(self, instance, validated_data):
        instance.menu_pic = validated_data.get('menu_pic', instance.menu_pic)
        instance.menu_name = validated_data.get(
            'menu_name', instance.menu_name)
        instance.menu_pri = validated_data.get('menu_pri', instance.menu_pri)
        instance.save()
        return instance


# Material Serializer
class MaterialSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

    # 신규 instance를 생성해서 리턴해준다
    def create(self, validated_data):
        return Material.objects.create(**validated_data)

        # 생성되어 있는 instance 를 저장한 후 리턴해준다
    def update(self, instance, validated_data):
        instance.mate_name = validated_data.get(
            'mate_name', instance.mate_name)
        instance.l_cat = validated_data.get('l_cat', instance.l_cat)
        instance.m_cat = validated_data.get('m_cat', instance.m_cat)
        instance.s_cat = validated_data.get('s_cat', instance.s_cat)
        instance.unit_cost = validated_data.get(
            'unit_cost', instance.unit_cost)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.save()
        return instance


# Ord 는 create 만 필요하고 수정은 필요하지 않다.
class OrdSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Ord
        fields = '__all__'

    # 신규 instance를 생성해서 리턴해준다
    def create(self, validated_data):
        return Ord.objects.create(**validated_data)

    # 생성되어 있는 instance 를 저장한 후 리턴해준다.
    # def update(self, instance, validated_data):
    #     instance.ord_num = validated_data.get('ord_num', instance.ord_num)
    #     instance.save()
    #     return instance


# CusOrd Serializer
class CusordSerializer(serializers.ModelSerializer):
    menu_id = MenuSerializer(read_only=True)

    class Meta:
        model = Cusord
        fields = '__all__'

    def create(self, validated_data):
        return Cusord.objects.create(**validated_data)


# InStock Serializer
class InstockSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    mate_id = MaterialSerializer(read_only=True)

    class Meta:
        model = Instock
        fields = '__all__'

    # 신규 instance를 생성해서 리턴해준다
    def create(self, validated_data):
        return Instock.objects.create(**validated_data)

    # 생성되어 있는 instance 를 저장한 후 리턴해준다
    def update(self, instance, validated_data):
        instance.in_time = validated_data.get('in_time', instance.in_time)
        instance.ord_num = validated_data.get('ord_num', instance.ord_num)
        instance.mate_id = validated_data.get('mate_id', instance.mate_id)
        instance.in_quan = validated_data.get('in_quan', instance.in_quan)
        instance.save()
        return instance


# Outstock 는 admin에서만 추가 수정 가능하면 충분하기 때문에 CRUD가 필요하지 않다.
class OutstockSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    mate_id = MaterialSerializer(read_only=True)
    cus_ord_num = CusordSerializer(read_only=True)

    class Meta:
        model = Outstock
        fields = '__all__'

# Recipe 는 admin에서만 추가 수정 가능하면 충분하기 때문에 CRUD가 필요하지 않다.


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

    # 신규 instance를 생성해서 리턴해준다
    # def create(self, validated_data):
    #     return Instock.objects.create(**validated_data)

        # 생성되어 있는 instance 를 저장한 후 리턴해준다
    def update(self, instance, validated_data):
        instance.man_name = validated_data.get('man_name', instance.man_name)
        instance.man_pw = validated_data.get('man_pw', instance.man_pw)
        instance.man_phone = validated_data.get(
            'man_phone', instance.man_phone)
        instance.man_addr = validated_data.get('man_addr', instance.man_addr)
        instance.man_mail = validated_data.get('man_mail', instance.man_mail)
        instance.man_safe = validated_data.get('man_safe', instance.man_safe)
        instance.biz_num = validated_data.get('biz_num', instance.biz_num)
        instance.save()
        return instance
