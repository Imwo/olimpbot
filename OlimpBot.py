import telebot
import sqlite3
from telebot import types

bot = telebot.TeleBot('1537716401:AAHYstpS7vejzbL5UkL5iahWfW7-4KxqBL8')

name = ''
surname = ''
level = 0


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message, "Чтобы начать напиши '/reg', если планируешь регистрироваться и '/noreg', если не будешь  ")


@bot.message_handler(commands=['reg'])
def send_registration(message):
    bot.send_message(message.from_user.id,
                     "Привет! Давай познакомимся! Как тебя зовут?")
    bot.register_next_step_handler(message, reg_name)


def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Какая у тебя фамилия?")
    bot.register_next_step_handler(message, reg_surname)


def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "В каком ты классе?")
    bot.register_next_step_handler(message, reg_level)


def reg_level(message):
    global level
    #age = message.text
    while level == 0:
        try:
            level = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "Вводите цифрами!")

    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Ты в ' + str(level) + \
        ' классе? И тебя зовут: ' + name + ' ' + surname + '?'
    bot.send_message(message.from_user.id, text=question,
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    try:
        if call.data == "yes":
            markup = types.InlineKeyboardMarkup(row_width=2)
            itembtn1 = types.InlineKeyboardButton(
                text='математика', callback_data='mathematics')
            itembtn2 = types.InlineKeyboardButton(
                text='физика', callback_data='physics')
            itembtn3 = types.InlineKeyboardButton(
                text='информатика', callback_data='informatics')
            markup.add(itembtn1, itembtn2, itembtn3)
            bot.send_message(call.message.chat.id,
                             "Выбери напрвление: ", reply_markup=markup)
        elif call.data == "no":
            bot.send_message(call.message.chat.id, "Попробуем еще раз!")
            bot.send_message(call.message.chat.id,
                             "Привет! Давай познакомимся! Как тебя зовут?")
            bot.register_next_step_handler(call.message, reg_name)
    except Exception as e:
        print(repr(e))


def callback_inline(call):
    try:
        if call.data == 'mathematics':
            bot.send_message(call.message.chat.id, 'Выбери класс:')
        elif call.data == 'physics':
            bot.send_message(call.message.chat.id, 'Выбери направление:')
        else:
            bot.send_message(call.message.chat.id, 'Выбери уровень:')
    except Exception as e:
        print(repr(e))


@bot.message_handler(commands=['noreg'])
def send_noregistration(message):
    keyboard = types.InlineKeyboardMarkup()
    key_mathematics = types.InlineKeyboardButton(
        text='Физика', callback_data='mathematics')
    keyboard.add(key_mathematics)
    key_physics = types.InlineKeyboardButton(
        text='Математика', callback_data='physics')
    keyboard.add(key_physics)
    key_informatics = types.InlineKeyboardButton(
        text='Информатика', callback_data='informatics')
    keyboard.add(key_informatics)
    bot.send_message(message.from_user.id,
                     "Давай заполним критерии, по которым ты будешь выбирать олимпиады. Выбери направление:", reply_markup=keyboard)


def send_answer(message):
    bot.send_message(message.chat.id, "Отлично! Теперь выбери направление")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, " Извини, я не понял твою команду(")


bot.polling()
