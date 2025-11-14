import telebot

TOKEN = "8215055578:AAGzCQ-eXBlr4nWSUhptsnJIJa2Q6Fc5BB8"
CHANNEL_LINK = "https://t.me/+7UaGyadgm2EwNTdi"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(
        "Присоединиться к каналу!", url=CHANNEL_LINK
    )
    keyboard.add(button)
    bot.send_message(message.chat.id, "Нажми на кнопку, чтобы присоединиться в канал:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    pass

bot.polling()
