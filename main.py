import random
import telebot
from telebot import types
from const import *
import time

bot = telebot.TeleBot(TOKEN)

# start command
@bot.message_handler(commands=['start'])
def start_command(message):
    name = message.from_user.first_name
    msg = f'Hi, nice to meet u, {name}! \nI`m your helper, <b>Mood Tracker</b> :):'
    bot.send_message(message.chat.id, msg, parse_mode='html')
    bot.send_message(message.chat.id, MSG[0], parse_mode='html', timeout=20)
    bot.send_sticker(message.chat.id, sticker=ICON)

# text command
@bot.message_handler(content_types=['text'])
def get_user_text(message):

    if message.text.lower() in HI_LIST:
        bot.send_message(message.chat.id, MSG[1], parse_mode='html')

    elif message.text.lower() in ['help']:
        bot.send_message(message.chat.id, MSG[2])
        bot.send_message(message.chat.id, MSG[3])

        # help buttons
        markup = types.InlineKeyboardMarkup(row_width=2)
        nrvbtn = types.InlineKeyboardButton('nervous', callback_data='nrv')
        sadbtn = types.InlineKeyboardButton('upset', callback_data='sad')
        markup.add(nrvbtn, sadbtn)

        bot.send_message(message.chat.id, MSG[4], reply_markup=markup)

    else:
        #helper
        bot.send_message(message.chat.id, MSG[5], parse_mode='html')

# sticker command
@bot.message_handler(content_types=['sticker'])
def get_user_sticker(message):
    name = message.from_user.first_name
    bot.send_message(message.chat.id, f'I understand, {name}\nLet`s move on!')

# callback command
@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):

    # end function of selfcare
    def proud_of_me():
        markup = types.InlineKeyboardMarkup(row_width=1)
        prdbtn = types.InlineKeyboardButton('sure', callback_data='prd')
        markup.add(prdbtn)
        bot.send_message(callback.message.chat.id, MSG[6], reply_markup=markup, parse_mode='html')

    # proud
    if callback.data == 'prd':
        bot.send_sticker(callback.message.chat.id, sticker=PROUD, timeout=30)
        bot.send_message(callback.message.chat.id, MSG[7])

    # nervous
    if callback.data == 'nrv':
        bot.send_sticker(callback.message.chat.id, sticker=NERVOUS, timeout=30)

        bot.send_message(callback.message.chat.id, MSG[8], timeout=20)
        bot.send_message(callback.message.chat.id, MSG[9], timeout=20)
        bot.send_message(callback.message.chat.id, MSG[10], timeout=20)

        for i in range(PERIOD):
            msg = MSG[11]
            if i != 0:
                msg += f'You`ve been working for {15*i} minutes!\n'
            if i != PERIOD:
                msg += f'There are {PERIOD-i} quarterts till the end!'
            bot.send_message(callback.message.chat.id, msg)
            moody_timer()

        bot.send_message(callback.message.chat.id, MSG[12])

        proud_of_me()

    # upset
    if callback.data == 'sad':
        bot.send_sticker(callback.message.chat.id, sticker=SAD, timeout=30)

        bot.send_message(callback.message.chat.id, MSG[13], timeout=20)
        bot.send_sticker(callback.message.chat.id, sticker=HERE, timeout=30)
        bot.send_message(callback.message.chat.id, MSG[14], timeout=20)

        markup = types.InlineKeyboardMarkup(row_width=1)
        trybtn = types.InlineKeyboardButton('🫂', callback_data='try')
        markup.add(trybtn)
        bot.send_message(callback.message.chat.id, MSG[15], reply_markup=markup, parse_mode='html')

    # choose upset tips
    if callback.data == 'try':
        msg = MSG[16] + random.choice(TIPS)
        bot.send_message(callback.message.chat.id, msg, parse_mode='html')

        bot.send_message(callback.message.chat.id, MSG[17])
        file_photo = 'photos/' + str(random.randint(1, 5)) + '.jpg'
        bot.send_photo(callback.message.chat.id, photo=open(file_photo, 'rb'))

        proud_of_me()

    # send upset tips
    if callback.data == 'tip':
        markup = types.InlineKeyboardMarkup(row_width=1)
        trybtn = types.InlineKeyboardButton('🫂', callback_data='try')
        markup.add(trybtn)
        bot.send_message(callback.message.chat.id, MSG[18], reply_markup=markup, parse_mode='html')

        proud_of_me()

# timer
def moody_timer():
    #time.sleep(MIN*60)
    # for testing it better try in short format
    time.sleep(MIN*60)

# help command
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, MSG[19])

# bot poll
bot.polling(none_stop=True)
