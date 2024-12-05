import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from flask import Flask, request

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
def setup_bot():
    updater = Updater(TELEGRAM_API_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    updater.start_polling()

# Set up Flask webhook route for Render
@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(), None)
    dispatcher = updater.dispatcher
    dispatcher.process_update(update)
    return 'OK'

# Start the Flask app and the Telegram bot
if __name__ == '__main__':
    setup_bot()
    app.run(host='0.0.0.0', port=5000)
