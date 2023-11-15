import logging
import uuid
from pathlib import Path
from telegram import Update
from telegram.ext import Updater, MessageHandler, CallbackContext, Filters
from .Steganography.Steganography import SteganographyImg

# Based on documentation from https://gitlab.com/Athamaxy/telegram-bot-tutorial/-/blob/main/TutorialBot.py
logger = logging.getLogger(__name__)


class TelegramBot(object):
    def __init__(self, token, tmp_dir):
        """Initialize the telegram bot

        :parameters token: Key probided by BotFather to access Telegram API
        :parameters token: Key probided by BotFather to access Telegram API
        """
        self.__token = token
        self.tmp_dir = Path(tmp_dir)
        self.updater = Updater(self.__token)
        # Get the dispatcher to register handlers
        # Then, we register each handler and the conditions the update must meet to trigger it
        dispatcher = self.updater.dispatcher
        dispatcher.add_handler(
            MessageHandler(Filters.document & Filters.caption,
                           self.encryptLSBImgText)
        )
        dispatcher.add_handler(
            MessageHandler(Filters.document, self.decryptLSBImg2Text)
        )
        logger.debug("Bot Initialization successful")
        pass

    def __generate_img_path(self, extension=".png"):
        img_name = str(uuid.uuid4()) + extension
        img_path = self.tmp_dir / img_name
        return img_path

    def __get_image(self, update: Update) -> str:
        bot = self.updater.bot
        file = bot.getFile(update.message.document.file_id)
        img_path = self.__generate_img_path()
        file.download(img_path.resolve())
        return img_path

    def encryptLSBImgText(self, update: Update, context: CallbackContext) -> None:
        logger.info("Calling Encrypt by LSB IMG+Text")
        # El mensaje a encriptar
        msg_to_encrypt = update.message.caption
        # Recibe la imagen
        img_path = self.__get_image(update)
        out_path = self.__generate_img_path()
        encrypt = SteganographyImg(
            img_path, out_path).encryptLSBImgText(msg_to_encrypt)
        if encrypt:
            out_img = open(out_path, "rb")
            context.bot.send_document(
                chat_id=update.effective_chat.id, document=out_img
            )
            out_img.close()
        pass

    def decryptLSBImg2Text(self, update: Update, context: CallbackContext) -> None:
        logger.info("Calling Decrypt  LSB IMG -> Text")
        img_path = self.__get_image(update)
        decrypted_msg = SteganographyImg(
            img_path, img_path).decryptLSBImg2Text()

        context.bot.send_message(
            chat_id=update.effective_chat.id, text=decrypted_msg)
        pass

    def run(self) -> None:
        """Start running the bot"""
        # Start the Bot
        self.updater.start_polling()
        # Run the bot until you press Ctrl-C
        self.updater.idle()


if __name__ == "__main__":
    print("attempting to call a module as a main")
    exit(1)
