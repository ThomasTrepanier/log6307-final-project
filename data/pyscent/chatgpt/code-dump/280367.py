from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Replace 'YOUR_BOT_TOKEN' with the token obtained from BotFather
bot_token = 'YOUR_BOT_TOKEN'
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

# Define the /start command handler
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I am your Telegram bot.")

# Define the echo message handler
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Create handlers and add them to the dispatcher
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)

# Start the bot
updater.start_polling()
updater.idle()
