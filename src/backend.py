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
def look_up_tweet() :
    query = tweets_ref.where(u'HasBeenTweeted', u'==', False).limit(1)
    docs = query.stream()

    for doc in docs :
        return doc
    
    return None

# Fetch a tweet and set it's "HasBeenTweeted" to true
def use_tweet() :
    tweet = look_up_tweet()
    
    if tweet == None :
        return None
    
    tweets_ref.document(tweet.id).update({u'HasBeenTweeted' : True})

    return tweet

# Fetches the number of tweets that have not been tweeted yet
def untweeted_tweets_count() :
    query = tweets_ref.where(u'HasBeenTweeted', u'==', False)
    docs = list(query.stream())
    return len(docs)

# Fetches the number of all tweets in the database
def total_tweet_count() :
    docs = list(tweets_ref.get())
    return len(docs)

# Fetches the number of tweets by a specific user, that have not been tweeted yet
def untweeted_tweets_by_user(username) :
    if type(username) != str :
        return None

    query = tweets_ref.where(u'Username', u'>=', username.upper())\
                    .where(u'Username', u'<=', username.lower() + u'\uf8ff')
    query = query.where(u'HasBeenTweeted', u'==', False)
    docs = list(query.stream())
    return len(docs)

# Fetches the number of all tweets by a specific user
def total_tweets_by_user(username) :
    if type(username) != str :
        return None

    query = tweets_ref.where(u'Username', u'>=', username.upper())\
                    .where(u'Username', u'<=', username.lower() + '\uf8ff')
    docs = list(query.stream())
    return len(docs)

# Add a tweet to the database
def add_tweet(text, username) :
    tweet = {
        u'HasBeenTweeted': False,
        u'Time': datetime.utcnow(),
        u'Text': text,
        u'Username': username
    }

    docId = tweets_ref.document().id
    tweets_ref.document(docId).set(tweet)

    return tweet
