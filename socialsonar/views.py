# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
      return render(request, 'socialsonar/index.html', {})

def ping(request, latitude, longitude):
      latitude = float(latitude)
      longitude = float(longitude)
      return HttpResponse('Huhro ping from {}, {}'.format(latitude, longitude))
