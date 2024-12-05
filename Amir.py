from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from flask import Flask
import os

app = Flask(__name__)

# Simple route to keep the app running
@app.route('/')
def home():
    return "Bot is running"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Hello! I am your bot, deployed on Render.')

def main():
    # Retrieve the bot token from environment variable
    token = "7783184735:AAFvd6LC3Py0vtHN6yTKvIXWMOC-TTWGcmM"
    if not token:
        raise ValueError("No TELEGRAM_TOKEN found in environment variables!")

    # Create the Application instance
    application = Application.builder().token(token).build()

    # Add command handler
    application.add_handler(CommandHandler("start", start))

    # Start the bot (this will continue running)
    application.run_polling()

    # Start Flask to keep the app running
    port = os.getenv("PORT", 5000)  # Render will provide the port
    app.run(host="0.0.0.0", port=int(port))  # Use Render's dynamic PORT

if __name__ == '__main__':
    main()
