# Create your views here.

import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from twitter import *
import cmath

consumer_key = "O5Z1KINSBaDEQgTBB3FA"
consumer_secret = "kf42pzVoDrmP4hoe9LNQW5t765J2zEspqdHQhotw"
access_key = "2172397754-TrCNJSgVarJIMnYb6uLXFzfI76zI7m8cfy5zIvL"
access_secret = "FNiDwwbgs0WiElgaJ2hVECnsyavUKIQ3IP7JNr4BkiOhx"# create twitter API object
auth = OAuth(access_key, access_secret, consumer_key, consumer_secret)
twitter = Twitter(auth = auth)

def home(request):
    return render_to_response('index.html', {})

def ping(request, latitude, longitude):
    # Convert latitude and longitude to floating point type
    latitude = float(latitude)
    longitude = float(longitude)
	
    # Query twitter API
    tweets = tweetsFromGeo(latitude, longitude)
	
    # Create list of tweets, sorted by theta
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

    # Build a JSON response out of it
    return HttpResponse(json.dumps(data), content_type="application/json")
    
def tweetsFromGeo(latitude, longitude, radius="1m"):
    geocode = "%s,%s,%s" % (latitude, longitude, radius)
    query = twitter.search.tweets(geocode = geocode, count=50)
    tweets = []
    for result in query["statuses"]:
        tweets.append(result)
    return tweets
    
