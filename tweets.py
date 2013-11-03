#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search
#  - performs a basic keyword search for tweets containing the keywords
#    "lazy" and "dog"
#-----------------------------------------------------------------------

from twitter import *

# create twitter API object
consumer_key = "O5Z1KINSBaDEQgTBB3FA"
consumer_secret = "kf42pzVoDrmP4hoe9LNQW5t765J2zEspqdHQhotw"
access_key = "2172397754-TrCNJSgVarJIMnYb6uLXFzfI76zI7m8cfy5zIvL"
access_secret = "FNiDwwbgs0WiElgaJ2hVECnsyavUKIQ3IP7JNr4BkiOhx"

# create twitter API object
auth = OAuth(access_key, access_secret, consumer_key, consumer_secret)
twitter = Twitter(auth = auth)


# request my home timeline
# twitter API docs: https://dev.twitter.com/docs/api/1/get/statuses/home_timeline
statuses = twitter.statuses.home_timeline(count = 50)

# loop through each of my statuses, and print its content
# for status in statuses:
# 	print "(%s) @%s %s" % (status["created_at"], status["user"]["screen_name"], status["text"])
#         

# query = twitter.search.tweets(geocode = "51.474144,-0.035401")
query = twitter.search.tweets(geocode = "38.95,-92.33,1mi")
for result in query["statuses"]:
	print "(%s) @%s %s" % (result["created_at"], result["id"], result["geo"])
