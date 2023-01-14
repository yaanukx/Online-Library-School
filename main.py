import telebot
from telebot import types
import admin

dict = {"Крылов И.А. Басни": 1,
"Жуковский В.А. Спящая красавица": 3}

bot = telebot.TeleBot("5712210975:AAHbtpqTH3nTi82NJoyf-JzoxTD65gVhhBc")
list = []
user = ''
@bot.message_handler(commands=["start"])
def message1(hello):
    message = bot.send_message(hello.chat.id, "Привет! Как тебя зовут?")
    bot.register_next_step_handler(message, get_user_text)

@bot.message_handler(commands=['text'])
def get_user_text(message):
    global user
    markup = types.InlineKeyboardMarkup()
    #markup.add(types.InlineKeyboardButton("Воспользоваться онлайн библиотекой", repeat_all_messages))
    bot.send_message(message.chat.id, f"Отлично {message.text} я тебя запомнил!")
    user = message.text

#@bot.message_handler(commands=['button'])
#def repeat_all_messages(message):
    # создаем клавиатуру
    keyboard = types.InlineKeyboardMarkup()

    # добавляем на нее две кнопки
    button1 = types.InlineKeyboardButton(text="Взять книгу", callback_data="button1")
    button2 = types.InlineKeyboardButton(text="Сдать книгу", callback_data="button2")
    keyboard.add(button1)
    keyboard.add(button2)

    # отправляем сообщение пользователю
    bot.send_message(message.chat.id, "Нажмите кнопку!", reply_markup=keyboard)
    list.append(message.text)

# функция запустится, когда пользователь нажмет на кнопку
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "button1":
            message = bot.send_message(call.message.chat.id, "Введить название книги в формате - автор(с большой буквы) + название(с большой буквы)")
            bot.register_next_step_handler(message, call_yes)
        if call.data == "button2":
            message = bot.send_message(call.message.chat.id, "Введите ваше имя")
            bot.register_next_step_handler(message, call_no)


def call_yes(message):
    global user
    if message.text in dict and dict[message.text] > 0:
        bot.send_message(message.chat.id, f"Вы можете взять книгу, в наличии {dict[message.text]}")
        dict[message.text] -= 1
        admin.send_noti(user,message.text)


def call_no(message):
    if message.text in list:
        bot.send_message(message.chat.id, "Вы можете вернуть книгу завтра")
    else:
        bot.send_message(message.chat.id, "У вас не активных книг")


bot.polling(none_stop=True)