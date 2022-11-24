import telebot.types
from telebot import TeleBot
bot = TeleBot('5498732265:AAHE1PuQe_8EyDLBpxnSAIpHzCHoErOIoFU')

@bot.message_handler(commands= ['help'])
def help(message):
    msg = bot.send_message(message.chat.id, " /calc - калькулятор")
    msg = bot.send_message(message.chat.id, " /wtf - генератор мата\n/phone телефонный справочник")
    # bot.register_next_step_handler(msg, user_answer)

@bot.message_handler(commands= ['calc'])
def calc(message):
    msg = bot.send_message(message.chat.id, "введите выражение типа (число) (действие) (число) "
                                            "разделяя вводимые значения и действие пробелом\n"
                                            "доступны действия + - * \\ ")
    bot.register_next_step_handler(msg, calc)
def calc(message):
    actions = ('+', '-', '*', '/')
    mess = message.text
    spl_mess = mess.split(' ')
    if spl_mess[0].isdigit() and spl_mess[2].isdigit():
        a = int(spl_mess[0])
        b = int(spl_mess[2])
        action = spl_mess[1]
        if action == '+':
            bot.send_message(message.chat.id, f"{a} + {b} = {a + b}")
        elif action == '-':
            bot.send_message(message.chat.id, f"{a} - {b} = {a - b}")
        elif action == '*':
            bot.send_message(message.chat.id, f"{a} * {b} = {a * b}")
        elif action == '/':
            bot.send_message(message.chat.id, f"{a} / {b} = {a / b}")
        else:
            msg = bot.send_message(message.chat.id, "введено некорректное/недоступное действие")


    else:
        bot.send_message(message.chat.id, "Введены некорректные данные ")
    msg = bot.send_message(message.chat.id, "Продолжим?")



    # if message.text == "":
    #     msg = bot.send_message(message.chat.id, " Что у тебя есть? ")
    #     bot.register_next_step_handler(msg, user_reg)
    # elif message == "нет":
    #     bot.send_message(message.chat.id, "нет? ")
    # else:
    #     bot.send_message(message.chat.id, " Што?) ")


def user_reg(message):
    bot.send_message(message.chat.id, f" Только {message.text} ??? ")




@bot.message_handler() # обработчик сообщения
def echo(msg: telebot.types.Message):
    if msg.text.lower() == 'привет':
        bot.send_message(chat_id=msg.from_user.id, text=' дароу 🤪 ')
    else:
        bot.send_message(chat_id=msg.from_user.id, text=msg.text + '? Чо?!')





bot.polling()