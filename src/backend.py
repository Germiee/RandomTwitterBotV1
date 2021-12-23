import firebase_admin
from loguru import logger
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
        printDocs()
    except :
        logger.error('Unable to connect to firebase!') 

def printDocs() :
    query = tweets_ref.where(u'HasBeenTweeted', u'==', False)#.limit(1)
    docs = query.stream()

    for doc in docs:
        logger.debug('{} => {} '.format(doc.id, doc.to_dict()))
