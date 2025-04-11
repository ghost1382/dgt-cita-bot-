from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import checker  # Make sure the checker file uses Playwright
import threading
import requests  # For sending Telegram messages
from playwright.sync_api import sync_playwright  # Import Playwright for browser automation

# Replace with your Telegram Bot token and chat ID
TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"  # Your chat ID for receiving messages

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
    result = checker.check_cita()
    await update.message.reply_text(f"Result of cita check: {result}")
    send_message(f"Result of cita check: {result}")

# Command to stop the bot
async def stop(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Bot stopped.")
    exit()

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
def start_periodic_check():
    check_thread = threading.Thread(target=checker.periodic_check)
    check_thread.daemon = True
    check_thread.start()

def main():
    # Start the periodic check in a separate thread
    start_periodic_check()

    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("check", check))
    application.add_handler(CommandHandler("stop", stop))
    application.add_handler(CommandHandler("help", help_command))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
