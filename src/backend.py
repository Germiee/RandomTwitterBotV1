import firebase_admin
from loguru import logger
from datetime import datetime
from firebase_admin import firestore
from firebase_admin import credentials

def __init__(firebase_file_path) :
    global tweets_ref

    try :
        cred = credentials.Certificate(firebase_file_path)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        tweets_ref = db.collection('Tweets')
        logger.info('Connected to firebase!')
    except :
        logger.error('Unable to connect to firebase!') 

# Fetch a tweet
def lookUpTweet() :
    query = tweets_ref.where(u'HasBeenTweeted', u'==', False).limit(1)
    docs = query.stream()

    for doc in docs :
        return doc
    
    return None

# Fetch a tweet and set it's "HasBeenTweeted" to true
def useTweet() :
    tweet = lookUpTweet()
    
    if tweet == None :
        return None
    
    tweets_ref.document(tweet.id).update({u'HasBeenTweeted' : True})

    return tweet

# Add a tweet to the database
def addTweet(text, username) :
    tweet = {
        u'HasBeenTweeted': False,
        u'Time': datetime.utcnow(),
        u'Text': text,
        u'Username': username
    }

    docId = tweets_ref.document().id
    tweets_ref.document(docId).set(tweet)

    return tweet
