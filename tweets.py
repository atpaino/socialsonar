#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search
#  - performs a basic keyword search for tweets containing the keywords
#    "lazy" and "dog"
#-----------------------------------------------------------------------

from twitter import *

import cmath

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

#query = twitter.search.tweets(geocode = "38.95,-92.33,1mi")
#tweets = []
#for result in query["statuses"]:
#    print "(%s) @%s %s" % (result["created_at"], result["id"], result["geo"])
#    tweets.append(result)

def tweetsFromGeo(latitude, longitude, radius="1m"):
    geocode = "%s,%s,%s" % (latitude, longitude, radius)
    query = twitter.search.tweets(geocode = "38.95,-92.33,1mi", count=50)
    tweets = []
    for result in query["statuses"]:
        tweets.append(result)
    return tweets

if __name__ == "__main__":

    latitude = float("38.95")
    longitude = float("-92.33")
    tweets = tweetsFromGeo(latitude, longitude)
    
    data = []
    
    for tweet in tweets:
        if tweet["geo"] is None:
            continue
        coords = tweet["geo"]["coordinates"]
        dx = latitude-coords[0]
        dy = longitude-coords[1]
        comp = complex(dx*69, dy*69)
        p = cmath.polar(comp)
        polar = [int(p[0]*100),p[1]]
        tweet =	{
            "id":tweet["id"],
            "text":tweet["text"],
            "source":tweet["source"],
            "user":	{
                "id":tweet["user"]["id"],
                "screen_name":tweet["user"]["screen_name"],
                "profile_image_url":tweet["user"]["profile_image_url"]
                },
            "polar":polar
            }
        data.append(tweet)
        
    print data