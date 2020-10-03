from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.

def welcome(request):
    return HttpResponse("<h1 style='color:blue'>Welcome To Django</h1>")


def topics(request):
    ct = str(datetime.datetime.now())
    return render(request, 'topics.html', {'now': ct})


def send_topics(request):
    topics = ['Templates', 'Views', 'Models', 'Ajax', 'Forms', 'ORM', 'REST']
    trainer = "Srikanth Pragada"
    return render(request, 'list_topics.html', {'topics': topics, 'trainer' : trainer})


def wish(request):
    if 'name' in request.GET:
        name = request.GET['name']
    else:
        name = "Guest"

    return HttpResponse(f"<h1>Hello, {name}</h1>")
