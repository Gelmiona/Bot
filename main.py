import random
from unittest.mock import call
import logging
import telebot
from telebot import types, callback_data  # для указание типов
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
token = '5533151079:AAHBCX_efMb2Kn7IgczPc0IoIX207pFc6HU'  # мой токен
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])  # если ввести команду \start
def start(message):
    # if message.chat.id not in res:
        # res[message.chat.id]=str(message.from_user.first_name)
    with open ('Пользователи.txt','a',encoding='utf-8') as file, open ('Пользователи.txt','r',encoding='utf-8') as file1 :
        a=file1.read()
        s=(f'{message.chat.id}:{message.from_user.first_name}\n')
        if s not in a:
                file.write(s)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # отсюда програмирование кнопок
    btn1 = types.KeyboardButton("Фридрих Ницше?")
    btn2 = types.KeyboardButton("Артур Шопенгауэр?")
    btn3 = types.KeyboardButton("Бенедикт Спиноза?")
    btn4 = types.KeyboardButton("А может неизвестный автор?")
    markup.add(btn1, btn2,btn3,btn4,row_width=1)
    bot.send_message(message.chat.id,
                     text='{0.first_name}, добрый день! Спасибо что заглянули! 🤝. Выберите,пожалуйста, интересующий Вас раздел 👇'.format(
                         message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Фридрих Ницше?"):
        with open ('Пользователи.txt','a',encoding='utf-8') as file, open ('Пользователи.txt','r',encoding='utf-8') as file1 :
            a=file1.read()
            s=(f'{message.chat.id}:{message.from_user.first_name}\n')
            if s not in a:
                file.write(s)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Цитату Фридриха?")
        btn2 = types.KeyboardButton("Интересные факты о Фридрихе")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back,row_width=2)
        file1 = open('Фридерих.jpg', 'rb')
        bot.send_photo(message.chat.id, file1)
        bot.send_message(message.chat.id, text="Фридрих Ницше – один из тех философов, слова которых зачастую толкуют не совсем верно."
                                               " И нетрудно догадаться, почему: его сочинения пространны – не всегда понятно, к чему именно клонит автор . Гораздо легче осмыслить великие идеи Ницше, изучив его афоризмы – краткие, но проницательные утверждения. Резкий формат высказываний идеально соответствует лаконичному, сосредоточенному на силе духу ницшеанской философии . Ницше даже недвусмысленно заявлял, что его «цель состояла в том, чтобы сказать в десяти предложениях то, чему другие посвящают целую книгу».", reply_markup=markup)


    elif (message.text == "Артур Шопенгауэр?"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Цитату Артура?")
        btn2 = types.KeyboardButton("Интересные факты о Артуре")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back,row_width=2)
        file1 = open('Артур.png', 'rb')
        bot.send_photo(message.chat.id, file1)
        bot.send_message(message.chat.id, text="Знаменитый немецкий философ XIX века Артур Шопенгауэр был известным мизантропом,"
                                               " закоренелым холостяком и любителем свободы. Но такое настороженное отношение к людям не помешало ему исследовать человеческую природу во всех ее проявлениях и рассказать о своих наблюдениях откровенно и категорично",reply_markup=markup)

    elif (message.text == "Бенедикт Спиноза?"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Цитату Бенедикта?")
        btn2 = types.KeyboardButton("Интересные факты о Бенедикте")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back,row_width=2)
        file1 = open('Бенедикт.jpg', 'rb')
        bot.send_photo(message.chat.id, file1)
        bot.send_message(message.chat.id, text="Нидерландский философ-рационалист и натуралист еврейского происхождения, один из главных представителей философии Нового времени. За свободомыслие был отлучён от еврейской общины; жил уединённо, зарабатывая на жизнь шлифовкой оптических стёкол; отклонил приглашение занять кафедру в Гейдельберге",reply_markup=markup)
    
    elif (message.text == "Цитату Артура?"):
        with open('Шопенгауэр.txt', 'r', encoding='utf-8') as file:
            res = file.readlines()
        bot.send_message(message.chat.id, random.choice(res))
        
    elif (message.text == "А может неизвестный автор?"):
        with open('Неизвестный.txt', 'r', encoding='utf-8') as file:
            res = file.readlines()
        bot.send_message(message.chat.id, random.choice(res))
        
    elif (message.text == "Интересные факты о Артуре"):
        with open('Факты о Шопенгауре.txt', 'r', encoding='utf-8') as file:
    #     bot.send_photo(message.chat.id, file):
            res = file.readlines()
            bot.send_message(message.chat.id, random.choice(res))

    elif (message.text == "Цитату Фридриха?"):
        with open('Ницше.txt', 'r', encoding='utf-8') as file:
            res = file.readlines()
        bot.send_message(message.chat.id, random.choice(res))
        
    elif (message.text == "Интересные факты о Фридрихе"):
        with open('Факты о Ницше.txt', 'r', encoding='utf-8') as file:
            res = file.readlines()
        bot.send_message(message.chat.id, random.choice(res))
          
    elif (message.text == "Цитату Бенедикта?"):
        with open('Бенедикт.txt', 'r', encoding='utf-8') as file:
            res = file.readlines()
        bot.send_message(message.chat.id, random.choice(res))
 
    elif (message.text == "Интересные факты о Бенедикте"):
        with open('Факты о Бенедикте.txt', 'r', encoding='utf-8') as file:
    #     bot.send_photo(message.chat.id, file):
            res = file.readlines()
        bot.send_message(message.chat.id, random.choice(res))

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # отсюда програмирование кнопок
        btn1 = types.KeyboardButton("Фридрих Ницше?")
        btn2 = types.KeyboardButton("Артур Шопенгауэр?")
        btn3 = types.KeyboardButton("Бенедикт Спиноза?")
        btn4 = types.KeyboardButton("А может неизвестный автор?")
        markup.add(btn1, btn2,btn3,btn4,row_width=1)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
        #row_width=2 #сколько кнопое ро горизонтали

    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован..")

bot.polling(none_stop=True)  # вечный цикд
# bot.infinity_polling