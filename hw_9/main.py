import telebot.types
from telebot import TeleBot
bot = TeleBot('5498732265:AAHE1PuQe_8EyDLBpxnSAIpHzCHoErOIoFU')

def summ(text):
    lst = text.split()
    if lst[0].isdigit() and lst[1].isdigit():
        return str(int(lst[0]) + int(lst[1]))
    return 'не корректный запрос'

@bot.message_handler()
def echo(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text= summ(msg.text))

bot.polling()

