import logging

from telegram import Update, ForceReply, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler

# Based on documentation from https://gitlab.com/Athamaxy/telegram-bot-tutorial/-/blob/main/TutorialBot.py
logger = logging.getLogger(__name__)

class TelegramBot:
    __token = None
    botname = None
    def __init__(self, token, botname):
        self.__token = token
        self.botname = botname

p1 = Person("John", 36)
    def main() -> None:
        updater = Updater("<YOUR_BOT_TOKEN_HERE>")

        # Get the dispatcher to register handlers
        # Then, we register each handler and the conditions the update must meet to trigger it
        dispatcher = updater.dispatcher

        # Register commands
        #dispatcher.add_handler(CommandHandler("scream", scream))

        # Start the Bot
        updater.start_polling()

        # Run the bot until you press Ctrl-C
        updater.idle()


if __name__ == '__main__':
    main()
