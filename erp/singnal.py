from django.db.models.signals import post_save
from django.dispatch import receiver
from erp.models import Menu,Cusord

@receiver( post_save,sender = Cusord)
def Cusord_post_save(sender,**kwargs):
    menu_id = kwargs['instance'].menu_id
    menu_id.menu_cnt += 1
    menu_id.save()