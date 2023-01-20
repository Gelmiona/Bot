
import random
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import logging

token='5533151079:AAHBCX_efMb2Kn7IgczPc0IoIX207pFc6HU'  # мой токен

proxy_url = 'http://proxy.server:3128'
bot = Bot(token=token, proxy=proxy_url)

dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])  # если ввести команду \start
async def start(message):
    # if message.chat.id not in res:
        # res[message.chat.id]=str(message.from_user.first_name)
    with open ('Пользователи.txt','a',encoding='utf-8') as file, open ('Пользователи.txt','r',encoding='utf-8') as file1 :
        a=file1.read()
        s=(f'{message.chat.id}:{message.from_user.first_name}\n')
        if s not in a:
                file.write(s)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)  # отсюда програмирование кнопок
    btn1 = types.KeyboardButton("Фридрих Ницше?")
    btn2 = types.KeyboardButton("Артур Шопенгауэр?")
    btn3 = types.KeyboardButton("Бенедикт Спиноза?")
    keyboard.add(btn1, btn2,btn3)
    await message.answer(text='{0.first_name}, добрый день! Спасибо что заглянули! 🤝. Выберите,пожалуйста, интересующий Вас раздел 👇'.format(
                         message.from_user), reply_markup=keyboard)

@dp.message_handler(content_types=['text'])
async def func(message):
    if (message.text == "Фридрих Ницше?"):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Цитату Фридриха?")
        btn2 = types.KeyboardButton("Интересные факты о Фридрихе")
        back = types.KeyboardButton("Вернуться в главное меню")
        keyboard.add(btn1, btn2, back)
        file1 = open('Фридерих.jpg', 'rb')
        await bot.send_photo(message.chat.id, file1)
        await message.answer(text="Фридрих Ницше – один из тех философов, слова которых зачастую толкуют не совсем верно."
                                               " И нетрудно догадаться, почему: его сочинения пространны – не всегда понятно, к чему именно клонит автор . Гораздо легче осмыслить великие идеи Ницше, изучив его афоризмы – краткие, но проницательные утверждения. Резкий формат высказываний идеально соответствует лаконичному, сосредоточенному на силе духу ницшеанской философии . Ницше даже недвусмысленно заявлял, что его «цель состояла в том, чтобы сказать в десяти предложениях то, чему другие посвящают целую книгу».", reply_markup=keyboard)


    elif (message.text == "Артур Шопенгауэр?"):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Цитату Артура?")
        btn2 = types.KeyboardButton("Интересные факты о Артуре")
        back = types.KeyboardButton("Вернуться в главное меню")
        keyboard.add(btn1, btn2, back)
        file1 = open('Артур.png', 'rb')
        await bot.send_photo(message.chat.id, file1)
        await message.answer(text="Знаменитый немецкий философ XIX века Артур Шопенгауэр был известным мизантропом,"
                                               " закоренелым холостяком и любителем свободы. Но такое настороженное отношение к людям не помешало ему исследовать человеческую природу во всех ее проявлениях и рассказать о своих наблюдениях откровенно и категорично",reply_markup=keyboard)

    elif (message.text == "Бенедикт Спиноза?"):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Цитату Бенедикта?")
        btn2 = types.KeyboardButton("Интересные факты о Бенедикте")
        back = types.KeyboardButton("Вернуться в главное меню")
        keyboard.add(btn1, btn2, back)
        file1 = open('Бенедикт.jpg', 'rb')
        await bot.send_photo(message.chat.id, file1)
        await message.answer(text="Нидерландский философ-рационалист и натуралист еврейского происхождения, один из главных представителей философии Нового времени. За свободомыслие был отлучён от еврейской общины; жил уединённо, зарабатывая на жизнь шлифовкой оптических стёкол; отклонил приглашение занять кафедру в Гейдельберге",reply_markup=keyboard)

    elif (message.text == "Цитату Артура?"):
        with open('Шопенгауэр.txt', 'r', encoding='utf-8') as file:
            res = file.readlines()
        await message.answer(random.choice(res))

    elif (message.text == "Интересные факты о Артуре"):
        with open('Факты о Шопенгауре.txt', 'r', encoding='utf-8') as file:
    #     bot.send_photo(message.chat.id, file):
            res = file.readlines()
            await message.answer(random.choice(res))

    elif (message.text == "Цитату Фридриха?"):
        with open('Ницше.txt', 'r', encoding='utf-8') as file:
            res = file.readlines()
        await bot.send_message(message.chat.id, random.choice(res))

    elif (message.text == "Интересные факты о Фридрихе"):
        with open('Факты о Ницше.txt', 'r', encoding='utf-8') as file:
            res = file.readlines()
        await bot.send_message(message.chat.id, random.choice(res))

    elif (message.text == "Цитату Бенедикта?"):
        with open('Бенедикт.txt', 'r', encoding='utf-8') as file:
            res = file.readlines()
        await bot.send_message(message.chat.id, random.choice(res))

    elif (message.text == "Интересные факты о Бенедикте"):
        with open('Факты о Бенедикте.txt', 'r', encoding='utf-8') as file:
    #     bot.send_photo(message.chat.id, file):
            res = file.readlines()
        await bot.send_message(message.chat.id, random.choice(res))

    elif (message.text == "Вернуться в главное меню"):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)  # отсюда програмирование кнопок
        btn1 = types.KeyboardButton("Фридрих Ницше?")
        btn2 = types.KeyboardButton("Артур Шопенгауэр?")
        btn3 = types.KeyboardButton("Бенедикт Спиноза?")
        keyboard.add(btn1, btn2,btn3)
        await message.answer(text="Вы вернулись в главное меню", reply_markup=keyboard)
        #row_width=2 #сколько кнопое ро горизонтали

    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован..")

executor.start_polling(dp, skip_updates=False)