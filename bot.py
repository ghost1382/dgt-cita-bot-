from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import logging
import threading
import os
import requests  # For sending Telegram messages
import checker  # Assuming you have the checker module

# Replace with your Telegram Bot token and chat ID
TOKEN = "7282237386:AAHFresU1mMc7kMlakjFjG-SkkxW7alV-Yk"
CHAT_ID = "7668015737"  # Your chat ID for receiving messages

# Add logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    response = requests.post(url, data=data)
    return response.status_code == 200

# Command to start the bot
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Bot started! Checking for citas...")

# Command to manually trigger a cita check
async def check(update: Update, context: CallbackContext) -> None:
    logger.info("Check command triggered!")  # Log when check is called
    result = checker.check_cita()
    await update.message.reply_text(f"Result of cita check: {result}")
    send_message(f"Result of cita check: {result}")

# Command to stop the bot
async def stop(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Bot stopped.")
    logger.info("Stopping the bot.")
    os._exit(0)  # Properly terminate the bot process

# Command to display help text
async def help_command(update: Update, context: CallbackContext) -> None:
    help_text = (
        "Available commands:\n\n"
        "/start - Start the bot and begin checking for citas.\n"
        "/check - Manually trigger a cita check.\n"
        "/stop - Stop the bot.\n"
        "/help - Show this help message."
    )
    await update.message.reply_text(help_text)

# Function to start periodic checks
async def check_periodically(context: CallbackContext):
    logger.info("Performing periodic cita check...")  # Log when periodic check happens
    result = checker.check_cita()
    context.bot.send_message(chat_id=CHAT_ID, text=f"Result: {result}")

def main():
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # Set up the job queue for periodic checks (every 30 minutes)
    job_queue = application.job_queue
    job_queue.run_repeating(check_periodically, interval=1800, first=0)

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("check", check))
    application.add_handler(CommandHandler("stop", stop))
    application.add_handler(CommandHandler("help", help_command))

    # Start the bot with polling and handle re-tries if needed
    application.run_polling(timeout=30, clean=True)

if __name__ == '__main__':
    main()
