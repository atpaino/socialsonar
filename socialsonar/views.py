# Create your views here.

import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from twitter import *

consumer_key = "O5Z1KINSBaDEQgTBB3FA"
consumer_secret = "kf42pzVoDrmP4hoe9LNQW5t765J2zEspqdHQhotw"
access_key = "2172397754-TrCNJSgVarJIMnYb6uLXFzfI76zI7m8cfy5zIvL"
access_secret = "FNiDwwbgs0WiElgaJ2hVECnsyavUKIQ3IP7JNr4BkiOhx"# create twitter API object
auth = OAuth(access_key, access_secret, consumer_key, consumer_secret)
twitter = Twitter(auth = auth)

def home(request):
    return render(request, 'socialsonar/index.html', {})

def ping(request, latitude, longitude):
    # Convert latitude and longitude to floating point type
    latitude = float(latitude)
    longitude = float(longitude)
	
    # Query twitter API
    tweets = tweetsFromGeo(latitude, longitude)
	
    # Create list of tweets, sorted by theta
    data = []
    for tweet in tweets:
        if tweet["geo_enabled"] is False:
            continue
        tweet =	{
            "id":tweet["id"],
            "text":tweet["text"],
            "source":tweet["source"],
            "user":	{
                "id":tweet["user"]["id"],
                "screen_name":tweet["user"]["screen_name"],
                "profile_image_url":tweet["user"]["profile_image_url"]
                },
            "geo":{
                "latitude":tweet["geo"]["coodrinates"][0],
                "longitude":tweet["geo"]["coodrinates"][1]
                }
            }
        data.append(tweet)

    # Build a JSON response out of it
    return HttpResponse(json.dumps(data), content_type="application/json")
    
def tweetsFromGeo(latitude, longitude, radius="1m"):
    query = twitter.search.tweets(geocode = "%f,%f,%s" % (latitude, longitude, radius))
    tweets = []
    for result in query["statuses"]:
        tweets.append(result)
    return tweets
    
