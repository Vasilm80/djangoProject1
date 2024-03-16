# Generated by Django 5.0.2 on 2024-03-02 08:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message_id', models.IntegerField(verbose_name='Идентификатор сообщения')),
                ('Message_text', models.TextField(verbose_name='Текст сообщения')),
                ('Chat_id', models.BigIntegerField(verbose_name='Идентификатор чата')),
                ('Message_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата сообщения')),
                ('Message_ans_status', models.BooleanField(default=False, verbose_name='Статус ответа')),
            ],
            options={
                'verbose_name': 'Сообщения',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_id', models.BigIntegerField(verbose_name='Идетификатор пользователя')),
                ('name', models.CharField(max_length=300, verbose_name='Имя пользователя')),
            ],
            options={
                'verbose_name': 'Пользователи',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Answer_text', models.TextField(verbose_name='Текст ответа')),
                ('Answer_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата')),
                ('Answer_status', models.BooleanField(default=False, verbose_name='Статус ответа')),
                ('Message_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.message', verbose_name='Идентификатор сообщения')),
            ],
            options={
                'verbose_name': 'Ответы',
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.CreateModel(
            name='Send_schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Period', models.CharField(choices=[('sec', 'seconds'), ('min', 'minutes'), ('hour', 'hour'), ('day', 'day')], verbose_name='Период рассылки')),
                ('Quanty', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('Text', models.TextField(verbose_name='Текст')),
                ('All', models.BooleanField(verbose_name='Всем пользователям')),
                ('User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Рассылки',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.AddField(
            model_name='message',
            name='User_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.user', verbose_name='Идетификатор пользователя'),
        ),
    ]