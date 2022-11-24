import telebot.types
from telebot import TeleBot
bot = TeleBot('5498732265:AAHE1PuQe_8EyDLBpxnSAIpHzCHoErOIoFU')

@bot.message_handler(commands= ['help'])
def help(message):
    msg = bot.send_message(message.chat.id, " да или нет? ")
    bot.register_next_step_handler(msg, user_answer)


def user_answer(message):
    if message.text == "да":
        msg = bot.send_message(message.chat.id,text= " да или нет? ")
        bot.register_next_step_handler(msg, user_reg)




@bot.message_handler() # обработчик сообщения
def echo(msg: telebot.types.Message):
    if msg.text.lower() == 'привет':
        bot.send_message(chat_id=msg.from_user.id, text=' дароу 🤪 ')
    else:
        bot.send_message(chat_id=msg.from_user.id, text=msg.text + '? Чо?!')





bot.polling()