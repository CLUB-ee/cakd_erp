# Generated by Django 3.2.5 on 2022-09-20 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_menu_menu_sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='stock',
            field=models.IntegerField(db_column='stock', default=0),
        ),
    ]
