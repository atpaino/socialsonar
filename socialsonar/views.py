# Create your views here.

import json

from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
      return render_to_response('index.html', {})

def ping(request, latitude, longitude):
      # Convert latitude and longitude to floating point type
      latitude = float(latitude)
      longitude = float(longitude)

      # Query twitter API
      tweets = []
      # TODO

      # Create list of tweets, sorted by theta
      data = []
      for tweet in tweets:
          data.append('hey')
      # TODO

      # Build a JSON response out of it
      return HttpResponse(json.dumps(data), content_type="application/json")
