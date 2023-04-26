from django.db.models.signals import post_save
from django.dispatch import receiver
from erp.models import Cusord, Instock, Outstock, Recipe

"""
Cusord 모델 인스턴스가 저장될 때 menu_id 객체의 menu_cnt 속성을 1 증가시키고, 
이와 연관된 Recipe 모델 인스턴스들을 이용하여 Outstock 모델 인스턴스를 생성하고, 
각각의 mate_id 객체의 stock 속성을 업데이트하는 작업을 수행하는 시그널 리시버 함수.
"""


@receiver(post_save, sender=Cusord)
def Cusord_post_save(sender, **kwargs):
    menu_id = kwargs['instance'].menu_id
    menu_id.menu_cnt += 1
    menu_id.save()

    ord_menu_recipe = Recipe.objects.filter(
        menu_id=kwargs['instance'].menu_id.menu_id)

    for i in ord_menu_recipe:
        # menuid = i.menu_id
        mateid = i.mate_id
        usage = i.mate_usage
        Outstock(cus_ord_num=kwargs['instance'],
                 mate_id=mateid, out_quan=usage).save()
        mateid.stock -= usage
        mateid.save()


"""Instock 모델 인스턴스가 저장될 때 mate_id 객체의 stock 속성을 업데이트하는 작업을 수행하는 시그널 리시버 함수"""


@ receiver(post_save, sender=Instock)
def Cusord_post_save(sender, **kwargs):
    instock_ = kwargs['instance'].mate_id
    instock_.stock += kwargs['instance'].in_quan
    instock_.save()
