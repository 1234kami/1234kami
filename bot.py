
import telebot
from telebot import types

botTimeWeb = telebot.TeleBot('6469426423:AAGN4PRrCBbvpvdXbhjYI3DBpgUDb0kgiyM')

@botTimeWeb.message_handler(commands=['start'])
def startBot(message):
    first_mess = f"<b>{message.from_user.first_name}</b>, привет!\nХочешь расскажу немного о себе?"
    markup = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text='Давай', callback_data='yes')
    markup.add(button_yes)
    button_why = types.InlineKeyboardButton(text='Зачем?', callback_data='why')
    markup.add(button_why)
    botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

@botTimeWeb.callback_query_handler(func=lambda call: True)
def response(function_call):
    if function_call.message:
        if function_call.data == "yes":
            second_mess = "Я Таалайбек кызы Камила, скоро мне исполнится 18!!!"
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://www.google.com/search?channel=fs&client=ubuntu-sn&q=%40Kamila2043"))
            botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            botTimeWeb.answer_callback_query(function_call.id)
        elif function_call.data == 'why':
            second_mess = "Ну, тогда)"
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("facebook", url="https://avtokafe.ru/Facebook/KamilTaalaibek kuzu"))
            botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            botTimeWeb.answer_callback_query(function_call.id)
        elif function_call.data == 'ну':
            second_mess = "мм"
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Можешь нажать", url="https://instagram/programist_9456"))
            botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            botTimeWeb.answer_callback_query(function_call.id)
botTimeWeb.infinity_polling()
