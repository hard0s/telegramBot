import config
import telebot
from main import bot, message
bot = bot


f = open ("ksk2 27/Fri.txt", "r", encoding = "utf-16LE")
read7 = f.read()


def test():
    if message.text == "понедельник":
        bot.send_message(message.chat.id, read7)

