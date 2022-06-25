import tweepy
from loguru import logger

global client

#def __init__(api_key, api_secret, access_token, access_secret) :
def __init__(twitter_bearer_token) :    
    try :
        # auth = tweepy.OAuthHandler(api_key, api_secret)
        # auth.set_access_token(access_token, access_secret)
        
        # client = tweepy.API(auth)

        client = tweepy.Client(bearer_token = twitter_bearer_token)

        client.create_tweet(text="#Python Rocks!")

        logger.info('Connected to twitter!')

        #get_new_messages()
    except Exception as e:
        # Just print(e) is cleaner and more likely what you want,
        # but if you insist on printing message specifically whenever possible...
        logger.error('Unable to connect to twitter!')
        if hasattr(e, 'message'):
            logger.error("Error message: " +e.message)
        else:
            logger.error(e) 

def get_new_messages() :
    toReturn = []
    cursor = -1
    messages = client.get_direct_messages(50, cursor)

    for m in messages:
        logger.info(m.message_create.message_data.text)

        
