from threading import Timer
import twitter_communications as twitter
import backend
from loguru import logger

def __init__(api:twitter, backend:backend):
    global _api
    global _backend
    
    _api = api
    _backend = backend
    messageTimer = Timer(1800.0, check_messages)
    messageTimer.start()


def check_messages():
    messages = _api.get_new_messages()

    for mes in messages:
        text = mes.message_create["message_data"]["text"]
        sender_name = _api.get_user_name(mes.message_create["sender_id"])
        _backend.add_tweet(text, sender_name)