from twitter import Api
from loguru import logger


def __init__(api_key, api_secret, access_token, access_secret) :
    global api
    try :
        api = Api(  api_key,
                    api_secret,
                    access_token,
                    access_secret)
        logger.debug('Followers: ', api.GetFollowers())
    except:
        logger.error('Unable to connect to twitter!')