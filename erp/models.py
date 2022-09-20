from configparser import MAX_INTERPOLATION_DEPTH
from django.db import models
from django.db.models import Q

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

# Create your models here.

class Menu(models.Model):
    menu_id = models.AutoField(db_column='menuId', primary_key=True)
    menu_pic = models.ImageField(
        db_column='menuPic', upload_to='erp/menu/imgaes/', blank=True, null=True)
    menu_name = models.CharField(db_column='menuName', max_length=20)
    menu_pri = models.IntegerField(db_column='menuPri')
    menu_cnt = models.IntegerField(db_column='menuCnt',default=0) # 주문카운트
    menu_sum = models.IntegerField(db_column='menuSum',default=0) # 합계

    class Meta:
        db_table = 'menu'

    def __str__(self):
        return f"{self.menu_id}:{self.menu_name}"

class Cusord(models.Model):
    cus_ord_num = models.AutoField(db_column='cusOrdNum', primary_key=True)
    out_time = models.DateTimeField(db_column='outTime', auto_now_add=True)
    menu_id = models.ForeignKey('Menu', models.DO_NOTHING, db_column='menuId')

    class Meta:
        db_table = 'cusOrd'

    def __str__(self):
        return str(self.cus_ord_num)


class Instock(models.Model):
    in_num = models.AutoField(db_column='inNum', primary_key=True)
    in_time = models.DateTimeField(db_column='inTime', auto_now_add=True)
    ord_num = models.ForeignKey('Ord', models.DO_NOTHING, db_column='ordNum')
    mate_id = models.ForeignKey(
        'Material', models.DO_NOTHING, db_column='mateId')
    in_quan = models.IntegerField(db_column='inQuan',default=0)
    in_total = models.IntegerField(db_column='inTotal',default=0)

    class Meta:
        db_table = 'inStock'

    def __str__(self):
        return str(self.in_num)


class Manager(models.Model):
    man_id = models.AutoField(db_column='manId', primary_key=True)
    man_name = models.CharField(db_column='manName', max_length=10)
    man_pw = models.CharField(db_column='manPw', max_length=20)
    man_phone = models.CharField(db_column='manPhone', max_length=15)
    man_addr = models.CharField(db_column='manAddr', max_length=50)
    man_mail = models.CharField(
        db_column='manMail', max_length=50, blank=True, null=True)
    man_safe = models.FloatField(db_column='manSafe')
    biz_num = models.CharField(
        db_column='bizNum', unique=True, max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'manager'

    def __str__(self):
        return self.man_name


class Material(models.Model):
    mate_id = models.AutoField(db_column='mateId', primary_key=True)
    mate_name = models.CharField(db_column='mateName', max_length=20)
    l_cat = models.CharField(
        db_column='lCat', max_length=10, blank=True, null=True)
    m_cat = models.CharField(
        db_column='mCat', max_length=10, blank=True, null=True)
    s_cat = models.CharField(
        db_column='sCat', max_length=10, blank=True, null=True)
    unit_cost = models.IntegerField(
        db_column='unitCost', blank=True, null=True)
    stock = models.IntegerField(db_column='stock',default=0)

    class Meta:
        db_table = 'material'

    def __str__(self):
        return str(self.mate_name)




# 발주
class Ord(models.Model):
    ord_num = models.AutoField(db_column='ordNum', primary_key=True)
    in_time = models.DateTimeField(db_column='inTime', auto_now_add=True)

    class Meta:
        db_table = 'ord'

    def __str__(self):
        return str(self.ord_num)


class Outstock(models.Model):
    out_num = models.AutoField(db_column='outNum', primary_key=True)
    out_time = models.DateTimeField(db_column='outTime', auto_now_add=True)
    cus_ord_num = models.ForeignKey(
        'Cusord', models.DO_NOTHING, db_column='cusOrdNum')
    mate_id = models.ForeignKey(
        'Material', models.DO_NOTHING, db_column='mateId')
    out_quan = models.IntegerField(db_column='outQuan',default=0)

    class Meta:
        db_table = 'outStock'

    def __str__(self):
        return str(self.out_num)


class Recipe(models.Model):
    menu_id = models.ForeignKey(Menu, models.DO_NOTHING, db_column='menuId')
    mate_id = models.ForeignKey(
        Material, models.DO_NOTHING, db_column='mateId')
    mate_usage = models.IntegerField(
        db_column='mateUsage', blank=True, null=True)

    class Meta:
        db_table = 'recipe'

    def __str__(self):
        return Menu.objects.filter(self.menu_id == 'menu_id')
