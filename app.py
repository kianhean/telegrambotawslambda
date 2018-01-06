import hug
import telepot
from telepot.exception import TelegramError
import json


bot = telepot.Bot("<TELEGRAMAPIKEY>")


@hug.post('/')
def receive(body):
    """ Simple Hug Server """
    output = handle(body)
    return output


def read_message(message):
    """ Returns Message as Dictionary """

    if isinstance(message, dict):
        message = message['message']
    else:
        message = json.loads(message)['message']

    return message


def handle(message):
    """ Handle JSON Message from Telegram
        message - string
        http://telepot.readthedocs.io/en/latest/reference.html
    """

    message = read_message(message)
    content_type, chat_type, chat_id = telepot.glance(message)

    try:
        if 'text' in message:
            if message['text'] == '/start':
                bot.sendMessage(
                    chat_id, text="Hi! I am working!", parse_mode="Markdown")
            else:
                # Dont deal with messages without text
                bot.sendMessage(
                    chat_id, text="Sorry we did not understand your request", parse_mode="HTML")
            return True

    except:
        bot.sendMessage(
            chat_id, text="Sorry we did not understand your request", parse_mode="HTML")
