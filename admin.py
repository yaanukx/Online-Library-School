from telebot import TeleBot

bot = TeleBot("5867414683:AAHrAZHpJSJN_NTTLxydIIzsJbKlXwIx54Q")
chat_id = 1068802759
@bot.message_handler(commands = ['help', 'start'])
def start (message):
    bot.reply_to (message,  """ \
Здравствуйте, Ольга Васильевна
Сюда вам будут приходить уведомления о бронирование книг
""")
def send_noti(name,book):
    bot.send_message(chat_id,f'{name} взял книгу {book} ')

if __name__=='__main__':
    bot.polling(none_stop=True)