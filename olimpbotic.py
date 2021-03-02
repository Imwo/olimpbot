import telebot #импортируем библиотеки
import sqlite3
import datetime
from telebot import types

bot = telebot.TeleBot('TOKEN')

name = ''
surname = ''
level = 0


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message, "Чтобы начать напиши '/reg', если планируешь регистрироваться и '/noreg', если не будешь  ")#вступительное сообщение


@bot.message_handler(commands=['reg'])# процесс регистрации
def send_registration(message):
    bot.send_message(message.from_user.id,
                     "Привет! Давай познакомимся! Как тебя зовут?")
    bot.register_next_step_handler(message, reg_name)# получаем имя


def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Какая у тебя фамилия?")
    bot.register_next_step_handler(message, reg_surname)# получаем фамилию


def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "В каком ты классе?")
    bot.register_next_step_handler(message, reg_level)# получаем класс ученика


def reg_level(message):
    global level
    while level == 0:
        try:
            level = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "Вводите цифрами!")# проверка на правильно введение

    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Ты в ' + str(level) + \
        ' классе? И тебя зовут: ' + name + ' ' + surname + '?'
    bot.send_message(message.from_user.id, text=question,
                     reply_markup=keyboard) # уточняем верны ли данные пользователя


@bot.callback_query_handler(lambda query: query.data in ["yes", "no"]) 
def callback_worker(query):
    try:
        if query.data == "yes":
            bot.send_message(
                query.message.chat.id, "Приятно познакомиться! Для продолжения нажми '/continue')")
        elif query.data == "no":
            bot.send_message(query.message.chat.id, "Попробуем еще раз!") # повторное введение данных
            bot.send_message(query.message.chat.id,
                             "Привет! Давай познакомимся! Как тебя зовут?")
            bot.register_next_step_handler(query.message, reg_name)
    except Exception as e:
        print(repr(e))


@bot.message_handler(commands=['continue'])
def inline_key(a):
    mainmenu = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Физика', callback_data='key1')
    key2 = types.InlineKeyboardButton(text='Информатика', callback_data='key2')
    key8 = types.InlineKeyboardButton(text='Математика', callback_data='key8')
    mainmenu.add(key1, key2, key8)
    bot.send_message(a.chat.id, 'Выбери направление', reply_markup=mainmenu) # выбор направлений


@bot.callback_query_handler(func=lambda call: True) # после выбора направления кнопки сменяются кнопками выбора уровней
def callback_inline(call):
    con=sqlite3.connect('olimpiads.db', check_same_thread=False)
    cur = con.cursor()
    cur.execute('create table if not exists list_olimps (name text, subject text, level integer, date date)')
    con.commit()
    if call.data == "mainmenu":
        mainmenu = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Физика', callback_data='key1')
        key2 = types.InlineKeyboardButton(
            text='Информатика', callback_data='key2')
        key8 = types.InlineKeyboardButton(
            text='Математика', callback_data='key8')
        mainmenu.add(key1, key2, key8)
        bot.edit_message_reply_markup(
            call.message.chat.id, call.message.message_id, reply_markup=mainmenu)
    elif call.data == "key1":
        next_menu = types.InlineKeyboardMarkup()
        key3 = types.InlineKeyboardButton(text='1', callback_data='key3')
        key5 = types.InlineKeyboardButton(text='2', callback_data='key5')
        key6 = types.InlineKeyboardButton(text='3', callback_data='key6')
        back = types.InlineKeyboardButton(
            text='Назад', callback_data='mainmenu')
        next_menu.add(key3, key5, key6, back)
        bot.edit_message_text('Выбери уровень:', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu)
        bot.send_message(call.message.chat.id, "Олимпиада школьников «Физтех»")
        bot.send_message(call.message.chat.id, "Олимпиада «Росатом»")
        bot.send_message(call.message.chat.id, "«Покори Воробьевы горы!»")              
    elif call.data == "key2":
        next_menu2 = types.InlineKeyboardMarkup()
        key4 = types.InlineKeyboardButton(text='1', callback_data='key11')
        key10 = types.InlineKeyboardButton(text='2', callback_data='key10')
        key7 = types.InlineKeyboardButton(text='3', callback_data='key7')
        back = types.InlineKeyboardButton(
            text='Назад', callback_data='mainmenu')
        next_menu2.add(key4, key10, key7, back)
        bot.edit_message_text('Выбери уровень:', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu2)
        bot.send_message(call.message.chat.id, "Олимпиада «Высшая проба»")
        bot.send_message(call.message.chat.id, "Всесибирская олимпиада школьников")
        bot.send_message(call.message.chat.id, "Олимпиада школьников «Ломоносов»")
        bot.send_message(call.message.chat.id, "Олимпиада по программированию «ТехноКубок»")
        
    elif call.data == "key8":
        next_menu2 = types.InlineKeyboardMarkup()
        key9 = types.InlineKeyboardButton(text='1', callback_data='key9')
        key13 = types.InlineKeyboardButton(text='2', callback_data='key13')
        key12 = types.InlineKeyboardButton(text='3', callback_data='key12')
        back = types.InlineKeyboardButton(
            text='Назад', callback_data='mainmenu')
        next_menu2.add(key9, key13, key12, back)
        bot.edit_message_text('Выбери уровень:', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu2)



@bot.message_handler(commands=['noreg'])# единоразовое пользование
def send_noreg(message):
    bot.reply_to(message, "В каком ты классе? ")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "5":
        bot.send_message(message.from_user.id,
                         "Принял, нажми '/continue', чтобы продолжить") # для продолжения возвращаемся к команде 'continue'
    elif message.text == "6":
        bot.send_message(message.from_user.id,
                         "Принял, нажми '/continue', чтобы продолжить")
    elif message.text == "7":
        bot.send_message(message.from_user.id,
                         "Принял, нажми '/continue', чтобы продолжить")
    elif message.text == "8":
        bot.send_message(message.from_user.id,
                         "Принял, нажми '/continue', чтобы продолжить")
    elif message.text == "9":
        bot.send_message(message.from_user.id,
                         "Принял, нажми '/continue', чтобы продолжить")
    elif message.text == "10":
        bot.send_message(message.from_user.id,
                         "Принял, нажми '/continue', чтобы продолжить")
    elif message.text == "11":
        bot.send_message(message.from_user.id,
                         "Принял, нажми '/continue', чтобы продолжить")
    else:
        bot.send_message(message.from_user.id,
                         "Я тебя не понимаю. Напиши /help.")


@bot.message_handler(func=lambda message: True) # в случае введения команды, которую бот не может распознать
def echo_all(message):
    bot.reply_to(message, " Извини, я не понял твою команду(")


bot.polling(none_stop=True, interval=0) # спрашивавет у бота не пришли ли ему новые сообщения
