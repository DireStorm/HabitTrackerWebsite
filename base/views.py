from django.shortcuts import render

# Create your views here.

#Function Based Views

#These are just for practice (you typically don't want to create views - renderings - in the urls file)
def home(request):
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html')