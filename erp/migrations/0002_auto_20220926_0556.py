# Generated by Django 3.2.12 on 2022-09-26 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='menu_cnt',
            field=models.IntegerField(db_column='menuCnt', default=0),
        ),
        migrations.AlterField(
            model_name='menu',
            name='menu_sum',
            field=models.IntegerField(db_column='menuSum', default=0),
        ),
    ]
