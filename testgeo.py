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

# perform a basic search 
# twitter API docs: https://dev.twitter.com/docs/api/1/get/search
query = twitter.search(q = "lazy dog")

# print how quickly the search completed
print "Search complete (%f seconds)" % (query["completed_in"])

# loop through each of my statuses, and print its content
for result in query["results"]:
        print "(%s) @%s %s" % (result["created_at"], result["from_user"], result["text"])
