import os
import telebot
from flask import Flask, request

# Получаем токен и вебхук из Environment
TOKEN = os.environ.get("TOKEN")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

# Проверка переменных
if not TOKEN:
    raise ValueError("TOKEN is not set! Check Environment Variables.")
if not WEBHOOK_URL:
    raise ValueError("WEBHOOK_URL is not set! Check Environment Variables!")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

CHANNEL_LINK = "https://t.me/+7UaGyadgm2EwNTdi"

# --------- Обработка команды /start ---------
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(
        "🔥 Присоединиться к каналу!", url=CHANNEL_LINK
    )
    keyboard.add(button)
    bot.send_message(
        message.chat.id,
        "Нажми на кнопку, чтобы присоединиться в канал:",
        reply_markup=keyboard
    )

# --------- Callback (пока пустой) ---------
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    pass

# --------- Webhook для Render ---------
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get("content-type") == "application/json":
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "OK", 200
    return "Unsupported Media Type", 403

@app.route('/')
def index():
    return "Bot is running!", 200

# --------- Запуск ---------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    
    # Установка webhook
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)

    app.run(host="0.0.0.0", port=port)
