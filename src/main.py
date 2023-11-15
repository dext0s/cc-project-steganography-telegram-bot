import os
import datetime
import logging
from  pathlib import Path
from TelegramBot.TelegramBot import TelegramBot

ENV_VAR_TOKEN = "TELEGRAM_BOT_TOKEN"
ENV_VAR_TEMPDIR = "TELEGRAM_BOT_TEMP_DIR"
def handle_exceptions(default_response):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                # Call the original function
                return func(*args, **kwargs)
            except Exception as e:
                # Handle the exception and provide the default response
                logging.exception(e)
                print(e)
                return default_response
        return wrapper
    return decorator

# Example usage
@handle_exceptions(default_response="Whoopsie! something went wrong, check the logs!")
def main() -> None:
    # Building temporal directory
    tb_tempdir = Path(os.getenv(ENV_VAR_TEMPDIR, "./bot_tmp"))
    os.makedirs(tb_tempdir.resolve(), exist_ok=True)
    #Setting up logging
    loggingFilename=datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S") + "_telegramBot.log"
    logging_path= tb_tempdir / loggingFilename
    logging.basicConfig(filename=logging_path.resolve(), level=logging.NOTSET)
    logging.info('Getting environment variables')
    # Get configuration from environment for the bot
    tb_token = os.getenv(ENV_VAR_TOKEN, None)
    if tb_token == None:
        raise Exception("Missing environment variable to define: " + ENV_VAR_TOKEN)
    logging.info('Initialazing Bot')
    tbot=TelegramBot(tb_token,tb_tempdir)
    logging.info('Running Bot')
    tbot.run()


if __name__ == '__main__':
    main()
