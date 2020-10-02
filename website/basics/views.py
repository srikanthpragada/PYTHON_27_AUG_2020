from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.

def welcome(request):
    return HttpResponse("<h1 style='color:blue'>Welcome To Django</h1>")


def topics(request):
    ct = str(datetime.datetime.now())
    return render(request, 'topics.html', {'now': ct})
