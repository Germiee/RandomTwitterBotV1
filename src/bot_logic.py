from email import message
from threading import Timer
import twitter_communications as twitter
import backend
from loguru import logger

def __init__(api:twitter, backend:backend):
    global _api
    global _backend
    global tweetTimer
    global messageTimer
    _api = api
    _backend = backend

    messageTimer = Timer(1800.0, check_messages) 

    tweetTimer = Timer(3600.0, tweet_making)

    messageTimer.start()
    tweetTimer.start()

def check_messages():
    
    logger.debug("Looking for new messages to add")
    messages = _api.get_new_messages()
    startMessageTimer()
    for mes in messages:
        logger.debug("Going through all new messages")
        _api.delete_message(mes.id) #This should theoretically delete the direct message 
        text = mes.message_create["message_data"]["text"]
        sender_name = _api.get_user_name(mes.message_create["sender_id"])
        _backend.add_tweet(text, sender_name)
    

def tweet_making():
    logger.debug("Making tweet probably")
    doc = _backend.look_up_tweet()
    _api.do_tweet(doc.get("Text")) # not properly documented, love
    # Gt tweet from backend, then do tweeting. pog

    startTweetTimer()

def startTweetTimer():
    tweetTimer = Timer(300.0, tweet_making)
    tweetTimer.start()

def startMessageTimer():
    messageTimer = Timer(900.0, check_messages) 
    messageTimer.start()
