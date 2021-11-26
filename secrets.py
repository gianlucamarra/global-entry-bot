twitter_credentials = dict(consumer_key= 'nODFKjiYzrF19xYefvQ6V1Npp',
                          consumer_secret= 'OI0ubjR7i3G2VfFzqzeZuehuh7ytyuZeSHPar9zI8qXPXjfSzC',
                          access_token_key= '1463947072403652618-scdxO96qAWUFoGePy4ZLSoDmLRBeys',
                          access_token_secret= 'LQipk1e8UWMIvhKgKPwhETEFIJ8UprzMfHppvPL8CrDqB')

message=input('first tweet')
api = twitter.Api(**twitter_credentials)
api.PostUpdate(message)
