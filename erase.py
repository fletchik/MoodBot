import telebot
import configure
from telebot import types

TOKEN = '5649889760:AAGPoeKDgpWD4OsEVdX9zbQQulFSHrE9jEg'

NERVOUS = 'CAACAgIAAxkBAAEGMIBjVuEqBsYiE2YzQyuXASmBPJqnNAACXyMAAqn9uEqlTuFkYmuJWioE'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    name = message.from_user.first_name
    msg = f'Hi, nice to meet u, {name}! \nI`m your helper, <b>Mood Tracker</b> :):'
    bot.send_message(message.chat.id, msg, parse_mode='html')
    msg = 'My name is Moody Body bot,\nI`ll help you with tracking your mood to keep you <b>being well and study hard!</b>'
    bot.send_message(message.chat.id, msg, parse_mode='html', timeout=20)
    bot.send_sticker(message.chat.id,
                     sticker="CAACAgIAAxkBAAEGMGRjVtbCGO08pZ1Do_7osgoQ76zX9gACcSUAAj25uUpXO0WzW2-pZioE")


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text.lower() in ['hi', 'hello', 'hi!', 'hello!']:
        msg = 'Sup, what`s cooking, good-looking?) \nIf u need a help, write <help>'
        bot.send_message(message.chat.id, msg)

    if message.text.lower() in ['help']:
        msg = 'Please, tell me about how ur feel rn?'
        bot.send_message(message.chat.id, msg)

        """msg = 'So tap on this sticker and send me the one from it, which describes U right now'
        bot.send_message(message.chat.id, msg)

        bot.send_sticker(message.chat.id, sticker="CAACAgIAAxkBAAEGMIpjVudRt3NlP1QbJ2ky47Tg9BcFowACjyMAAuCKsUqRLqTz3NnUUyoE")"""
        msg = '& I`ll send your some advices:'
        bot.send_message(message.chat.id, msg)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

        nrv = types.KeyboardButton('nervous')
        prd = types.KeyboardButton('proud')
        sad = types.KeyboardButton('sad')

        markup.add(nrv, prd, sad)

        bot.send_message(message.chat.id, 'choose your feeling:', reply_markup=markup)

    if message.text.lower() in ['nervous']:
        bot.send_sticker(message.chat.id, sticker=NERVOUS, timeout=30)
        msg = 'You can feel nervous about your deadlines. What`s your first priority task? I can set a reminder for u:'
        bot.send_message(message.chat.id, msg, timeout=45)

        msg = 'You will feel better, when u do your task, so right now start doing it. I`ll send you messages every 10 minutes for an hour'
        bot.send_message(message.chat.id, msg, timeout=20)

        msg = 'Try to concentrate, here`s your reminder for an hour:'
        bot.send_message(message.chat.id, msg, timeout=20)

    """if message.text.lower() in ['feel']:
        bot.send_message(message.chat.id, 'okey')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

        nrv = types.KeyboardButton('NERVOUS')
        prd = types.KeyboardButton('PROUD')
        sad = types.KeyboardButton('SAD')

        markup.add(nrv, prd, sad)

        bot.send_message(message.chat.id, '', reply_markup=markup)


    else:
        msg = 'If you need some help, ask for it! send me <i><b>help</b></i>'
        bot.send_message(message.chat.id, msg, parse_mode='html')"""


@bot.message_handler(content_types='sticker')
def get_user_sticker(message):
    name = message.from_user.first_name
    bot.send_message(message.chat.id, f'I understand, {name}')
    bot.send_message(message.chat.id, message.sticker.file_id)

    """if message.sticker.file_id == NERVOUS:
        bot.send_message(message.chat.id, 'u feel very nervous, isn`t it?')"""


"""@bot.message_handler()
def website(message):
    markup = types.ReplyKeyboardMarkup()

    nrv = types.ReplyKeyboardMarkup('NERVOUS')
    prd = types.ReplyKeyboardMarkup('PROUD')
    sad = types.ReplyKeyboardMarkup('SAD')

    markup.add(nrv, prd, sad)

    bot.send_message(message.chat.id, reply_markup=markup)"""


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, 'If you need some help, ask for it!')


bot.polling(none_stop=True)
