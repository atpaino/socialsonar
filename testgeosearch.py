#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search-geo
#  - performs a search for tweets close to New Cross, and outputs
#    them to a CSV file.
#-----------------------------------------------------------------------

from twitter import *

import sys
import csv

OAUTH_TOKEN = '2172397754-TrCNJSgVarJIMnYb6uLXFzfI76zI7m8cfy5zIvL'
OAUTH_SECRET = 'FNiDwwbgs0WiElgaJ2hVECnsyavUKIQ3IP7JNr4BkiOhx'
CONSUMER_KEY = 'O5Z1KINSBaDEQgTBB3FA'
CONSUMER_SECRET = 'kf42pzVoDrmP4hoe9LNQW5t765J2zEspqdHQhotw'

# create twitter API object
twitter = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
                       CONSUMER_KEY, CONSUMER_SECRET))

# open a file to write (mode "w"), and create a CSV writer object
csvfile = file("output.csv", "w")
csvwriter = csv.writer(csvfile)

# add headings to our CSV file
row = [ "user", "text", "latitude", "longitude" ]
csvwriter.writerow(row)


username = "slander36"

# the twitter API only allows us to query up to 100 tweets at a time.
# to search for more, we will break our search up into 10 "pages", each
# of which will include 100 matching tweets.
for pagenum in range(1, 11):

        # perform a search based on latitude and longitude
        # twitter API docs: https://dev.twitter.com/docs/api/1/get/search
#         query = twitter.statuses.filter(q = "", geocode = "51.474144,-0.035401,1km", rpp = 100, page = pagenum)
        query = twitter.statuses.filter(locations = "51.474144,-0.035401", rpp = 100, page = pagenum)
#         query = twitter.statuses.user_timeline(screen_name = username)

        for result in query["results"]:
                # only process a result if it has a geolocation
                if result["geo"]:
                        user = result["from_user"]
                        text = result["text"]
                        text = text.encode('ascii', 'replace')
                        latitude = result["geo"]["coordinates"][0]
                        longitude = result["geo"]["coordinates"][1]

                        # now write this row to our CSV file
                        row = [ user, text, latitude, longitude ]
                        csvwriter.writerow(row)

        # let the user know where we're up to
        print "done page: %d" % (pagenum)

# we're all finished, clean up and go home.
csvfile.close()