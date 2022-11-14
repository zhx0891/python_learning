import telebot.types
from telebot import TeleBot
bot = TeleBot('5498732265:AAHE1PuQe_8EyDLBpxnSAIpHzCHoErOIoFU')


@bot.message_handler() # обработчик сообщиения
def echo(msg: telebot.types.Message):
    if msg.text.lower() == 'привет':
        bot.send_message(chat_id=msg.from_user.id, text=' дароу 🤪 ')
    else:
        bot.send_message(chat_id=msg.from_user.id, text=msg.text + '? Чо?!')





bot.polling()