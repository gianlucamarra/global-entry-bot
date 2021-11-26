##twitter_credentials = dict(consumer_key= 'btji7ufQvgGcINzwZZ9pV1rbS',
                           ##consumer_secret= 'Q91KQW5IBXfnWZF8Y0rPB1SaKXF0wA2dxi51poS2r4BCZWtHDB',
                          ## access_token_key= '1463947072403652618-kk77vJEMYSuVCwBMdinH8GRUgnM3Pe',
                          ## access_token_secret= '41YXimkgAwIse628WW2t2JWo2POdj5IFz6H7wVdgtkBqc')
import numpy as np
import tweepy

#variables for accessing twitter API
consumer_key='btji7ufQvgGcINzwZZ9pV1rbS'
consumer_secret_key='Q91KQW5IBXfnWZF8Y0rPB1SaKXF0wA2dxi51poS2r4BCZWtHDB'
access_token='1463947072403652618-kk77vJEMYSuVCwBMdinH8GRUgnM3Pe'
access_token_secret='41YXimkgAwIse628WW2t2JWo2POdj5IFz6H7wVdgtkBqc'
      
auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
tweet=input('one time')
#Generate text tweet
api.update_status(tweet)
