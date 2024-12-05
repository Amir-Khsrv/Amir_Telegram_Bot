import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
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
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello! I am your simple bot.')

# Setup the Application and add handlers
async def setup_bot():
    application = Application.builder().token(TELEGRAM_API_TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    await application.initialize()

# Webhook route for Flask to handle requests from Telegram
@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(), None)
    application.update_queue.put(update)  # Feed the update to the application queue
    return 'OK'

# Set the webhook when running the app
async def set_webhook():
    webhook_url = 'https://amir-telegram-bot.onrender.com/webhook'
    application.bot.set_webhook(url=webhook_url)

# Start Flask app and set webhook
if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(setup_bot())  # Initialize the bot
    app.run(host='0.0.0.0', port=5000)
