import telebot.types
from telebot import TeleBot
bot = TeleBot('5498732265:AAHE1PuQe_8EyDLBpxnSAIpHzCHoErOIoFU')

def summ(text):
    lst = text.split()
    if len(lst) == 2 and lst[0].isdigit() and lst[1].isdigit():
        return str(int(lst[0]) + int(lst[1]))
    return 'не корректный запрос'




@bot.message_handler(commands=['log'])
def echo(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Лог программы \n ffffffffffffff')
    bot.send_document(chat_id=msg.from_user.id, document=open('TestBot.log', 'rb'))

@bot.message_handler(content_types=['document'])
def echo(msg: telebot.types.Message):
    file = bot.get_file(msg.document.file_id)
    downloaded_file = bot.download_file(file.file_path)
    with open((msg.document.file_name, 'wb')) as f_out:
        f_out.write(downloaded_file)


@bot.message_handler(commands=['help'])
def help_comm(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Справка')

@bot.message_handler()
def echo(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=summ(msg.text))

bot.polling()

