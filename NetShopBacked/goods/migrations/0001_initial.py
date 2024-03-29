# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-08 02:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x90\x8d')),
                ('goods_sn', models.CharField(default=b'', max_length=64, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x94\xaf\xe4\xb8\x80\xe8\xb4\xa7\xe5\x8f\xb7')),
                ('click_num', models.IntegerField(default=0, verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe6\x95\xb0')),
                ('sold_num', models.IntegerField(default=0, verbose_name=b'\xe9\x94\x80\xe5\x94\xae\xe6\x95\xb0')),
                ('fav_num', models.IntegerField(default=0, verbose_name=b'\xe6\x94\xb6\xe8\x97\x8f\xe6\x95\xb0')),
                ('goods_num', models.IntegerField(default=0, verbose_name=b'\xe5\xba\x93\xe5\xad\x98\xe6\x95\xb0')),
                ('market_price', models.FloatField(default=b'', verbose_name=b'\xe5\xb8\x82\xe5\x9c\xba\xe4\xbb\xb7')),
                ('shop_price', models.FloatField(default=b'', verbose_name=b'\xe6\x9c\xac\xe5\xba\x97\xe4\xbb\xb7\xe6\xa0\xbc')),
                ('goods_brief', models.TextField(default=b'', verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe7\xae\x80\xe4\xbb\x8b')),
                ('desc', models.TextField(default=b'', verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0\xe5\x86\x85\xe5\xae\xb9')),
                ('delivery_fee', models.FloatField(default=0.0, verbose_name=b'\xe8\xbf\x90\xe8\xb4\xb9')),
                ('is_new', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\xba\xe6\x96\xb0\xe5\x93\x81')),
                ('is_hot', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe7\x83\xad\xe9\x94\x80')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u5546\u54c1',
                'verbose_name_plural': '\u5546\u54c1',
            },
        ),
        migrations.CreateModel(
            name='GoodsBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x90\x8d')),
                ('desc', models.TextField(default=b'', verbose_name=b'\xe5\x93\x81\xe7\x89\x8c\xe6\x8f\x8f\xe8\xbf\xb0\xe4\xbf\xa1\xe6\x81\xaf')),
                ('img', models.ImageField(upload_to=b'brands/', verbose_name=b'\xe5\x93\x81\xe7\x89\x8c\xe5\xa4\xb4\xe5\x83\x8f')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u54c1\u724c',
                'verbose_name_plural': '\u5546\u54c1\u54c1\u724c',
            },
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text=b'\xe5\x95\x86\xe5\x93\x81\xe7\xb1\xbb\xe5\x88\xab', max_length=32, null=True, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe7\xb1\xbb\xe5\x88\xab')),
                ('code', models.CharField(blank=True, help_text=b'\xe5\x95\x86\xe5\x93\x81code', max_length=32, null=True, verbose_name=b'\xe5\x95\x86\xe5\x93\x81code')),
                ('desc', models.TextField(default=b'', help_text=b'\xe7\xb1\xbb\xe5\x88\xab\xe6\x8f\x8f\xe8\xbf\xb0', verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('category_type', models.SmallIntegerField(choices=[(0, b'\xe4\xb8\x80\xe7\xba\xa7\xe7\xb1\xbb\xe5\x88\xab'), (1, b'\xe4\xba\x8c\xe7\xba\xa7\xe7\xb1\xbb\xe5\x88\xab'), (2, b'\xe4\xb8\x89\xe7\xba\xa7\xe7\xb1\xbb\xe5\x88\xab')], default=0)),
                ('is_tab', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x9c\x89\xe5\xaf\xbc\xe8\x88\xaa\xe6\xa0\x8f')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
                ('parent_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='goods.GoodsCategory', verbose_name=b'\xe7\x88\xb6\xe7\xba\xa7\xe7\xb1\xbb\xe5\x88\xab')),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u7c7b\u522b',
                'verbose_name_plural': '\u5546\u54c1\u7c7b\u522b',
            },
        ),
        migrations.AddField(
            model_name='goodsbrand',
            name='catatory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='goods.GoodsCategory', verbose_name=b'\xe5\x93\x81\xe7\x89\x8c\xe7\xb1\xbb\xe5\x88\xab'),
        ),
        migrations.AddField(
            model_name='goods',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goods_to_brand', to='goods.GoodsBrand', verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe6\x89\x80\xe5\xb1\x9e\xe5\x93\x81\xe7\x89\x8c'),
        ),
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='goods.GoodsCategory', verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe6\x89\x80\xe5\xb1\x9e\xe7\xb1\xbb\xe5\x88\xab'),
        ),
    ]
