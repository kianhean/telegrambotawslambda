import hug
import telepot
from telepot.exception import TelegramError
import json


bot = telepot.Bot("<TELEGRAMAPIKEY>")


@hug.post('/')
def receive(body):
    """ Simple Hug Server """
    output = read_message(body)
    return output


def read_message(message):
    """ Returns Message as Dictionary """

    if not isinstance(message, dict):
        msg = json.loads(message)['message']
    else:
        msg = message
 
    if 'callback_query' in msg:
        on_callback_query(msg['callback_query'])
    elif 'message' in msg:
        on_chat_message(msg['message'])
        
    return 'OK'


def on_chat_message(message):
    """ Handle JSON Message from Telegram
        message - string
        http://telepot.readthedocs.io/en/latest/reference.html
    """
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
 
def on_callback_query(message):
    """
        do sth similar to on_chat_message
    """
    return
