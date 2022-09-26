# Generated by Django 3.2.5 on 2022-09-26 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cusord',
            fields=[
                ('cus_ord_num', models.AutoField(db_column='cusOrdNum', primary_key=True, serialize=False)),
                ('out_time', models.DateTimeField(auto_now_add=True, db_column='outTime')),
            ],
            options={
                'db_table': 'cusOrd',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('man_id', models.AutoField(db_column='manId', primary_key=True, serialize=False)),
                ('man_name', models.CharField(db_column='manName', max_length=10)),
                ('man_pw', models.CharField(db_column='manPw', max_length=20)),
                ('man_phone', models.CharField(db_column='manPhone', max_length=15)),
                ('man_addr', models.CharField(db_column='manAddr', max_length=50)),
                ('man_mail', models.CharField(blank=True, db_column='manMail', max_length=50, null=True)),
                ('man_safe', models.FloatField(db_column='manSafe')),
                ('biz_num', models.CharField(blank=True, db_column='bizNum', max_length=15, null=True, unique=True)),
            ],
            options={
                'db_table': 'manager',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('mate_id', models.AutoField(db_column='mateId', primary_key=True, serialize=False)),
                ('mate_name', models.CharField(db_column='mateName', max_length=20)),
                ('l_cat', models.CharField(blank=True, db_column='lCat', max_length=10, null=True)),
                ('m_cat', models.CharField(blank=True, db_column='mCat', max_length=10, null=True)),
                ('s_cat', models.CharField(blank=True, db_column='sCat', max_length=10, null=True)),
                ('unit_cost', models.IntegerField(blank=True, db_column='unitCost', null=True)),
                ('stock', models.IntegerField(db_column='stock', default=0)),
            ],
            options={
                'db_table': 'material',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.AutoField(db_column='menuId', primary_key=True, serialize=False)),
                ('menu_pic', models.ImageField(blank=True, db_column='menuPic', null=True, upload_to='erp/menu/imgaes/')),
                ('menu_name', models.CharField(db_column='menuName', max_length=20)),
                ('menu_pri', models.IntegerField(db_column='menuPri')),
                ('menu_cnt', models.IntegerField(db_column='menuCnt', default=0)),
                ('menu_sum', models.IntegerField(db_column='menuSum', default=0)),
            ],
            options={
                'db_table': 'menu',
            },
        ),
        migrations.CreateModel(
            name='Ord',
            fields=[
                ('ord_num', models.AutoField(db_column='ordNum', primary_key=True, serialize=False)),
                ('in_time', models.DateTimeField(auto_now_add=True, db_column='inTime')),
            ],
            options={
                'db_table': 'ord',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mate_usage', models.IntegerField(blank=True, db_column='mateUsage', null=True)),
                ('mate_id', models.ForeignKey(db_column='mateId', on_delete=django.db.models.deletion.DO_NOTHING, to='erp.material')),
                ('menu_id', models.ForeignKey(db_column='menuId', on_delete=django.db.models.deletion.DO_NOTHING, to='erp.menu')),
            ],
            options={
                'db_table': 'recipe',
            },
        ),
        migrations.CreateModel(
            name='Outstock',
            fields=[
                ('out_num', models.AutoField(db_column='outNum', primary_key=True, serialize=False)),
                ('out_time', models.DateTimeField(auto_now_add=True, db_column='outTime')),
                ('out_quan', models.IntegerField(db_column='outQuan', default=0)),
                ('cus_ord_num', models.ForeignKey(db_column='cusOrdNum', on_delete=django.db.models.deletion.DO_NOTHING, to='erp.cusord')),
                ('mate_id', models.ForeignKey(db_column='mateId', on_delete=django.db.models.deletion.DO_NOTHING, to='erp.material')),
            ],
            options={
                'db_table': 'outStock',
            },
        ),
        migrations.CreateModel(
            name='Instock',
            fields=[
                ('in_num', models.AutoField(db_column='inNum', primary_key=True, serialize=False)),
                ('in_time', models.DateTimeField(auto_now_add=True, db_column='inTime')),
                ('in_quan', models.IntegerField(db_column='inQuan', default=0)),
                ('in_total', models.IntegerField(db_column='inTotal', default=0)),
                ('mate_id', models.ForeignKey(db_column='mateId', on_delete=django.db.models.deletion.DO_NOTHING, to='erp.material')),
                ('ord_num', models.ForeignKey(db_column='ordNum', on_delete=django.db.models.deletion.DO_NOTHING, to='erp.ord')),
            ],
            options={
                'db_table': 'inStock',
            },
        ),
        migrations.AddField(
            model_name='cusord',
            name='menu_id',
            field=models.ForeignKey(db_column='menuId', on_delete=django.db.models.deletion.DO_NOTHING, to='erp.menu'),
        ),
    ]
