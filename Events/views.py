from django.shortcuts import render

from .models import Event

# Create your views here.


def home(requests):
    events = Event.objects
    return render(requests, "Events/home.html", {"events": events})
