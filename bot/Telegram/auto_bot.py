import datetime

import telebot
from environs import Env

import os
import django
from bs4 import BeautifulSoup
import requests



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'avto.settings')
django.setup()
from bot.models import User, Message
from av_by.models import Car
env = Env()
env.read_env()

bot = telebot.TeleBot(env.str('Token_bot'))

r = requests.get('https://select.by/kursy-valyut/natsbank-rb/dollar')
bs = BeautifulSoup(r.text,'lxml')

usd = bs.find('span', class_='font-size-3rem font-weight-500')


@bot.message_handler(commands=['start'])
def start_send(message):
    bot.send_message(message.chat.id,'Привет. Я бот. Что бы узнать что я могу напиши /help')
    us = User()
    us_all = User.objects.filter(User_id=message.chat.id)
    if not us_all:
        us.User_id = int(message.chat.id)
        us.name = message.from_user.full_name
        us.save()
@bot.message_handler(commands=['send_all'])
def send_all(message):
    if message.from_user.id == 	6098608035:
        users = User.objects.all()
        for user in users:
            bot.send_message(user.User_id, f'Добрый день, <b>{user.name}</b>. Обновлены мои возможности. Для справки нажми /help', parse_mode='html')
    else: bot.send_message(message.from_user.id, f'К сожалению у вас нет прав доступа к данной команде, <b>{message.from_user.full_name}</b>', parse_mode='html')


@bot.message_handler(commands=['help'])
def help_send(message):
    bot.send_message(message.chat.id, '''
    Команды для работы с ботом:
    /usd - получить курс доллара США
    /help - получить справку    
    /car - получить последние добавленные на сайте машины
    /BMW - получить список машин марки BMW
    /Reno - получить все машины марки Renault
    /All - получить все марки машин
    ''')
@bot.message_handler(commands=['usd'])
def dollar(message):
    bot.send_message(message.chat.id, f'Курс доллара {usd.text}')

@bot.message_handler(commands=['car'])
def car(message):
    cars = Car.objects.all()
    bot.send_message(message.chat.id,'Последние добавления:')
    for car in cars:
        if str(car.data_create)[0:9]==(str(datetime.date.today())[0:9]):
            bot.send_message(message.chat.id, f'<a href="http://localhost:3000/car/{car.id}">{car.mark_car} {car.model_car} </a>\n{car.year}г. \n Цена {car.price} р', parse_mode='html')

@bot.message_handler(commands=['BMW'])
def BMV(message):
    cars = Car.objects.filter(mark_car='BMW')
    for bmv in cars:
        bot.send_message(message.chat.id, f'''{bmv.mark_car} {bmv.model_car} \n 
{bmv.year} года 
Цена {bmv.price}р \n Продавец {bmv.user.name} 
Телефон +375{bmv.user.phone}''')

@bot.message_handler(commands=['All'])
def All(message):
    cars = Car.objects.all()
    marks = set()
    for car in cars:
        marks.add(car.mark_car)
    marks_arr = list(marks)
    marks_arr.sort()
    for i in marks_arr:
        bot.send_message(message.chat.id, f'{i}')

@bot.message_handler(commands=['Reno'])
def Reno(message):
    cars = Car.objects.filter(mark_car='Renault')
    for bmv in cars:
        bot.send_message(message.chat.id, f'''{bmv.mark_car} {bmv.model_car} 
{bmv.year} года 
Цена {bmv.price}р
Продавец {bmv.user.name} 
Телефон +375{bmv.user.phone}''')

@bot.message_handler(func=lambda message: True)
def echo(message):
    us = User.objects.get(User_id=message.chat.id)
    mes = Message()
    mes.Chat_id = message.chat.id
    mes.Message_id = message.id
    mes.Message_text = message.text
    mes.User_id = us
    mes.save()
    bot.send_message(message.chat.id, f'<b>{message.from_user.first_name}</b>, Ваш вопрос принят. Скоро на него будет ответ.', parse_mode="html")


bot.infinity_polling()