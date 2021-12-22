import tweepy
from loguru import logger


def __init__(api_key, api_secret, access_token, access_secret) :
    global client
    try :
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_secret)

        client = tweepy.API(auth)
        client.update_status("#Python Rocks!")
    except:
        logger.error('Unable to connect to twitter!')