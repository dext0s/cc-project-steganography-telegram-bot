import os 
import logging

ENV_VAR_TOKEN = "TELEGRAM_BOT_TOKEN"
ENV_VAR_BOT_NAME = "TELEGRAM_BOT_NAME"

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
@handle_exceptions(default_response="Whoopsie! something went Wrong, check the logs!")
def main() -> None:
    #Setting up logging 
    logging.basicConfig(filename='telegramBot.log', level=logging.NOTSET)
    logging.info('Starting Bot')
    logging.info('Getting environment variables')
    # Get configuration from environment for the bot
    tb_token = os.getenv(ENV_VAR_TOKEN, None)
    tb_name = os.getenv(ENV_VAR_BOT_NAME, None)
    if tb_name == None:
        raise Exception("Missing environment variable to define: " + ENV_VAR_BOT_NAME)
    if tb_token == None:
        raise Exception("Missing environment variable to define: " + ENV_VAR_TOKEN)
    pass



if __name__ == '__main__':
    main()
