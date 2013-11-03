#!/usr/bin/env python

# import twitter

# api = twitter.Api()
# 
# api = twitter.Api(consumer_key='O5Z1KINSBaDEQgTBB3FA',
# 	consumer_secret='kf42pzVoDrmP4hoe9LNQW5t765J2zEspqdHQhotw',
# 	access_token_key='2172397754-TrCNJSgVarJIMnYb6uLXFzfI76zI7m8cfy5zIvL',
# 	access_token_secret='FNiDwwbgs0WiElgaJ2hVECnsyavUKIQ3IP7JNr4BkiOhx')
# 	                     
# print api.VerifyCredentials()


# token = 'FNiDwwbgs0WiElgaJ2hVECnsyavUKIQ3IP7JNr4BkiOhx'
# token_key = '2172397754-TrCNJSgVarJIMnYb6uLXFzfI76zI7m8cfy5zIvL'
# con_secret = 'kf42pzVoDrmP4hoe9LNQW5t765J2zEspqdHQhotw'
# con_secret_key = 'O5Z1KINSBaDEQgTBB3FA'
# 
# # from twitter import Twitter
# twitter = Twitter(auth=OAuth(token, token_key, con_secret, con_secret_key))
# twitter.statuses.public_timeline()


from twython import Twython

APP_KEY = 'O5Z1KINSBaDEQgTBB3FA'
APP_SECRET = 'kf42pzVoDrmP4hoe9LNQW5t765J2zEspqdHQhotw'
OAUTH_TOKEN = '2172397754-TrCNJSgVarJIMnYb6uLXFzfI76zI7m8cfy5zIvL'
OAUTH_TOKEN_SECRET = 'FNiDwwbgs0WiElgaJ2hVECnsyavUKIQ3IP7JNr4BkiOhx'

twitter = Twython(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
print twitter.get_home_timeline()
print twitter.search(q='twitter')
print twitter.search(q='twitter', result_type='popular')