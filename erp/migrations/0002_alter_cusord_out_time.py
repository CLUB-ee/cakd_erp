# Generated by Django 3.2.5 on 2022-09-27 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cusord',
            name='out_time',
            field=models.DateField(auto_now_add=True, db_column='outTime'),
        ),
    ]