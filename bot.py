from telegram import Bot
from telegram.ext import Updater, CommandHandler
import checker

# Replace with your Telegram Bot token and chat ID
TOKEN = "7282237386:AAHFresU1mMc7kMlakjFjG-SkkxW7alV-Yk"
CHAT_ID = "7668015737"  # Your chat ID for receiving messages

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    response = requests.post(url, data=data)
    return response.status_code == 200

# Command to start the bot
def start(update, context):
    update.message.reply_text("Bot started! Checking for citas...")

# Command to manually trigger a cita check
def check(update, context):
    result = checker.check_cita()
    update.message.reply_text(f"Result of cita check: {result}")
    send_message(f"Result of cita check: {result}")

# Command to stop the bot
def stop(update, context):
    update.message.reply_text("Bot stopped.")
    exit()

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN, use_context=True)
    
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    
    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("check", check))
    dispatcher.add_handler(CommandHandler("stop", stop))
    
    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
