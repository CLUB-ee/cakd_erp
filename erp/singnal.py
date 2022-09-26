from django.db.models.signals import post_save
from django.dispatch import receiver
from erp.models import Menu, Cusord, Material, Instock, Outstock, Recipe


@receiver(post_save, sender=Cusord)
def Cusord_post_save(sender, **kwargs):
    menu_id = kwargs['instance'].menu_id
    menu_id.menu_cnt += 1
    menu_id.save()

    ord_menu_recipe = Recipe.objects.filter(
        menu_id=kwargs['instance'].menu_id.menu_id)
    # li = []
    for i in ord_menu_recipe:
        menuid = i.menu_id
        mateid = i.mate_id
        usage = i.mate_usage
        Outstock(cus_ord_num=kwargs['instance'],
                 mate_id=mateid, out_quan=usage).save()


@ receiver(post_save, sender=Instock)
def Cusord_post_save(sender, **kwargs):
    instock_ = kwargs['instance'].mate_id
    instock_.stock += kwargs['instance'].in_quan
    instock_.save()
