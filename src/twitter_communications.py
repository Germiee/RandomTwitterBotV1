import tweepy
from loguru import logger

# The Twitter account id of our bot, needed for several requests
# TODO add the option for an optional parameter to change this id
default_bot_id = "1332712271987023874" 


def __init__(api_key, api_secret, access_token, access_secret) :  
    try :
        # This grants access to the Twitter API V2
        # Sadly the V2 API does not have proper direct message handling yet (for some stupid reason)
        # client = tweepy.Client(
        #     consumer_key=api_key,
        #     consumer_secret=api_secret,
        #     access_token=access_token,
        #     access_token_secret=access_secret
        # )

        auth = tweepy.OAuth1UserHandler(
            api_key,
            api_secret,
            access_token,
            access_secret
        )

        client = tweepy.API(auth)

        logger.info('Connected to twitter!')

        return client
    except Exception as e:
        # Just print(e) is cleaner and more likely what you want,
        # but if you insist on printing message specifically whenever possible...
        logger.error('Unable to connect to twitter!')
        if hasattr(e, 'message'):
            logger.error("Error message: {}", e.message)
        else:
            logger.error("Error message: {}", e) 
        return None #we return none just so client variable is really lost

def get_new_messages(client) :
    logger.info("Trying to get direct messages")
    try :
        all_messages = client.get_direct_messages(count = 200)

        logger.info("Number of messages (Including the bots messages): {}", len(all_messages))

        new_messages = []
        for mes in all_messages:
            if mes.message_create["sender_id"] != default_bot_id :
                new_messages.append(mes)
            else : 
                logger.info("Found message from bot: {}", mes.message_create["message_data"]["text"])

        return new_messages
    except Exception as e:
        logger.error('Could not get direct messages')
        if hasattr(e, 'message'):
            logger.error("Error message: {}", e.message)
        else:
            logger.error("Error message: {}",e) 
        return None
    

        
def delete_message(client, id):
    logger.info("Deleting direct message with the ID: {}", id)
    try :
        client.delete_direct_message(id)
    except Exception as e:
        logger.error("Could not delete message")
        if hasattr(e, 'message'):
            logger.error("Error message: {}", e.message)
        else:
            logger.error("Error message: {}", e) 

def send_message(client, id, content):
    logger.info("Sending direct message to the user with the ID: {}", id)
    try :
        client.send_direct_message(id,content)
    except Exception as e:
        logger.error("Could not send message")
        if hasattr(e, 'message'):
            logger.error("Error message: {}", e.message)
        else:
            logger.error("Error message: {}", e) 
            