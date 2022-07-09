from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#Function Based Views

#These are just for practice (you typically don't want to create views - renderings - in the urls file)
def home(request):
    return HttpResponse("<h1>Jerin's Home Page</h1>")

def room(request):
    return HttpResponse("<p1>This is a ROOM sub url</p1>")