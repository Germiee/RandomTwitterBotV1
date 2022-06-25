import sys
import re
import backend
import bot_logic as bot
import twitter_communications as twitter
from loguru import logger

if len(sys.argv) == 8 :
    logger.debug('Scanning command line arguments!')

    TWEET_INTERVAL = sys.argv[1]
    FIREBASE_API_KEY_FILE_PATH = sys.argv[2]
    TWITTER_API_KEY = sys.argv[3]
    TWITTER_API_SECRET = sys.argv[4]
    TWITTER_ACCESS_TOKEN = sys.argv[5]
    TWITTER_ACCESS_SECRET = sys.argv[6]
    TWITTER_BEARER_TOKEN = sys.argv[7]

    logger.debug('Checking tweet interval!')
    if re.match('^\d\d?[HhMm]$',TWEET_INTERVAL) == None :
        logger.error('The tweet interval must look like this: 1h or 45m!')
    else : 
        logger.info('Bot is booting!')
        # TODO Start bot
        backend.__init__(FIREBASE_API_KEY_FILE_PATH)
        api = twitter.__init__(TWITTER_API_KEY,TWITTER_API_SECRET,TWITTER_ACCESS_TOKEN,TWITTER_ACCESS_SECRET)

        twitter.get_new_messages(api)
        #twitter.__init__(TWITTER_BEARER_TOKEN)
else :
    logger.error('Missing arguments!')
    logger.error('Usage: main.py <TWEET-INTERVAL> <FIREBASE-API-KEY-FILE-PATH> <TWITTER-API-KEY> <TWITTER-API-SECRET> <TWITTER-ACCESS-TOKEN> <TWITTER-ACCESS-SECRET> <TWITTER-BEARER-TOKEN>')
