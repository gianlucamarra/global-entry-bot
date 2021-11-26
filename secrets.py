#twitter_credentials = dict(consumer_key= "nODFKjiYzrF19xYefvQ6V1Npp",
                          #consumer_secret= "OI0ubjR7i3G2VfFzqzeZuehuh7ytyuZeSHPar9zI8qXPXjfSzC",
                          #access_token_key= "1463947072403652618-scdxO96qAWUFoGePy4ZLSoDmLRBeys",
                          #access_token_secret= "LQipk1e8UWMIvhKgKPwhETEFIJ8UprzMfHppvPL8CrDqB")
#importing all dependencies
import numpy as np
import tweepy

#variables for accessing twitter API
consumer_key='nODFKjiYzrF19xYefvQ6V1Npp'
consumer_secret_key='OI0ubjR7i3G2VfFzqzeZuehuh7ytyuZeSHPar9zI8qXPXjfSzC'
access_token='1463947072403652618-scdxO96qAWUFoGePy4ZLSoDmLRBeys'
access_token_secret='LQipk1e8UWMIvhKgKPwhETEFIJ8UprzMfHppvPL8CrDqB'
bearer_token='AAAAAAAAAAAAAAAAAAAAAHe8WAEAAAAAFOdG5KkJtdyPz05w%2FR2DYoJvs%2B4%3DpgO894Z6ltPgNyOqiiRJsjXgxTynzrybLmfegqzU8xJUGN0GkN'

#auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
#auth.set_access_token(access_token,access_token_secret)
#api=tweepy.API(auth)


#tweet=input('first tweet,yes')
#Generate text tweet
#api.status(tweet)

tweeter_obj = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret_key,
                            access_token=access_token, access_token_secret=access_token_secret,
                            wait_on_rate_limit=True)
message="here we go again"
response = tweeter_obj.create_tweet(text=message)
