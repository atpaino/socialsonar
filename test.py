#!/usr/bin/env python

import json
from twython import Twython

APP_KEY = 'O5Z1KINSBaDEQgTBB3FA'
APP_SECRET = 'kf42pzVoDrmP4hoe9LNQW5t765J2zEspqdHQhotw'
OAUTH_TOKEN = '2172397754-TrCNJSgVarJIMnYb6uLXFzfI76zI7m8cfy5zIvL'
OAUTH_TOKEN_SECRET = 'FNiDwwbgs0WiElgaJ2hVECnsyavUKIQ3IP7JNr4BkiOhx'

twitter = Twython(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
# 
# print twitter.search(q='twitter')
# print twitter.search(q='twitter', result_type='popular')
# print twitter.search(q='python', result_type='popular')
# print twitter.verify_credentials()
# twitter.update_status(status='See how easy using Twython is!')
print twitter.get_home_timeline()
content = twitter.search(q='geo', result_type='popular')
print content
# parsed = json.loads(content)
# json.dumps(parsed, indent=4, sort_keys=True)

# class MyStreamer(TwythonStreamer):
# 	def on_success(self, data):
# 		if 'text' in data:
# 			print data['text'].encode('utf-8')
# 	def on_error(self, status_code, data):
# 		print status_code
# 		
# stream = MyStreamer(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
# stream.statuses.filter(track='twitter')
