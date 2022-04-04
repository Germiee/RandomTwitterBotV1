import tweepy
from loguru import logger


def __init__(api_key, api_secret, access_token, access_secret) :
    global client
    try :
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_secret)

        client = tweepy.API(auth)
        client.update_status("#Python Rocks!")
        
        logger.info('Connected to twitter!')

        get_new_messages()
    except:
        logger.error('Unable to connect to twitter!')

def get_new_messages() :
    toReturn = []
    cursor = -1
    messages = client.get_direct_messages(50, cursor)

    for m in messages:
        logger.info(m.message_create.message_data.text)
