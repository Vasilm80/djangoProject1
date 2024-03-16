# Generated by Django 5.0.2 on 2024-03-02 08:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Город',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=9)),
                ('photo', models.ImageField(upload_to='static/photos/')),
                ('password', models.CharField(max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'Пользователи',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark_car', models.CharField(max_length=100, verbose_name='Марка')),
                ('model_car', models.CharField(max_length=100, verbose_name='Модель')),
                ('generation', models.CharField(max_length=100, verbose_name='Поколение')),
                ('body', models.CharField(max_length=100, verbose_name='Кузов')),
                ('motor', models.CharField(max_length=100, verbose_name='Топливо')),
                ('transmission', models.CharField(max_length=100, null=True, verbose_name='Коробка передач')),
                ('drive', models.CharField(max_length=100, verbose_name='Привод')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('volume', models.CharField(max_length=30, verbose_name='Объем двигателя')),
                ('photo', models.TextField(verbose_name='Фото')),
                ('vin', models.CharField(max_length=20, null=True)),
                ('data_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('mileage', models.IntegerField(default=0, verbose_name='Пробег')),
                ('color', models.CharField(max_length=20, null=True, verbose_name='Цвет')),
                ('condition', models.CharField(max_length=20, null=True, verbose_name='Состояние')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('exchange', models.CharField(max_length=40, null=True, verbose_name='Обмен')),
                ('options', models.TextField(null=True, verbose_name='Опции')),
                ('city_id', models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='av_by.city', verbose_name='Город')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='av_by.user', verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Машины',
                'verbose_name_plural': 'Машины',
            },
        ),
    ]
