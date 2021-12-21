import twitter
from loguru import logger


def __init__(_api_key,_api_secret,_access_token,_access_secret):
    global api
    api = twitter.Api(consumer_key=_api_key,
                      consumer_secret = _api_secret,
                      access_token = _access_token,
                      access_secret = _access_secret )
