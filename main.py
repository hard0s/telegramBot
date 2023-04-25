import telebot
from telebot import types
import config
import test1


bot = telebot.TeleBot(config.TOKEN)
 

@bot.message_handler(commands=['start'])
def get_user_info(message):
        
    markup_inline = types.InlineKeyboardMarkup()
    item_sis = types.InlineKeyboardButton(text="СисАдм 2/1", callback_data="sis")
    item_isip = types.InlineKeyboardButton(text="ИСИП 2/3", callback_data="isip")
    item_ksk = types.InlineKeyboardButton(text="КСК 2/27", callback_data="ksk")

    markup_inline.add(item_isip, item_sis, item_ksk)
    bot.send_message(message.chat.id, "выбери группу", reply_markup = markup_inline)

    @bot.callback_query_handler(func=lambda call: True)
    def answer_callback(call):
        if call.data == "sis":
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard= True)
            item_ID = types.KeyboardButton('MY ID')
            markup_reply.add(item_ID)
            bot.send_message(call.message.chat.id, "выбранна группа СисАдм 2/1", reply_markup = markup_reply)
        elif call.data == "isip":
            
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard= True)
            item_week = types.KeyboardButton('Неделя')
            item_mon = types.KeyboardButton('Понедельник')
            item_tue = types.KeyboardButton('Вторник')
            item_wed = types.KeyboardButton('Среда')
            item_thu = types.KeyboardButton('Четверг')
            item_fri = types.KeyboardButton('Пятница')
            
            markup_reply.add(item_mon, item_tue, item_wed, item_thu, item_fri, item_week )
            bot.send_message(call.message.chat.id, "выбранна группа ИСиП(п) 2/3", reply_markup = markup_reply)

        elif call.data == "ksk":
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard= True)
            item_week = types.KeyboardButton('Неделя')
            item_mon = types.KeyboardButton('Понедельник')
            item_tue = types.KeyboardButton('Вторник')
            item_wed = types.KeyboardButton('Среда')
            item_thu = types.KeyboardButton('Четверг')
            item_fri = types.KeyboardButton('Пятница')
            
            markup_reply.add(item_mon, item_tue, item_wed, item_thu, item_fri, item_week )
            bot.send_message(call.message.chat.id, "КСК 2/27", reply_markup = markup_reply)

        elif call.data == "test":
            bot.send_message(call.message.chat.id, test1.get_user_message)


@bot.message_handler()
@bot.callback_query_handler(func=lambda call: True)
def answer_callback(call):
    def get_user_message(message):
        if message.text == "понедельник" & call.data == "ksk":
            bot.send_message(message.chat.id, test1.read7)





bot.infinity_polling()
