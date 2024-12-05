import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, Dispatcher
from flask import Flask, request
import os

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Flask app for Render
app = Flask(__name__)

# Your bot's token here
TELEGRAM_API_TOKEN = '7946706520:AAHxnfqdrH6Km7QP-AnM3xYwEcZzvKaCJN8'

# Define the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your simple bot.')

# Setup the Updater and Dispatcher
updater = Updater(TELEGRAM_API_TOKEN)
dispatcher: Dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))

# Webhook route for Flask to handle requests from Telegram
@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(), None)
    dispatcher.process_update(update)
    return 'OK'

# Set the webhook when running the app
def set_webhook():
    webhook_url = 'https://amir-telegram-bot.onrender.com/webhook'
    updater.bot.set_webhook(url=webhook_url)

# Start Flask app and set webhook
if __name__ == '__main__':
    set_webhook()  # Set the webhook for your bot
    app.run(host='0.0.0.0', port=5000)
