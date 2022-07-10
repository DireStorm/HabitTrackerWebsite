from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view #decorator import
from .models import UInfo
from .serializers import UInfoSerializer

# Create your views here.

#Function Based Views

#These are just for practice (you typically don't want to create views - renderings - in the urls file)
@api_view(['GET']) #Decorator for API  usability 
def home(request):
    return Response("<h1> Jerin's Website </h1>")

@api_view(['GET'])
def room(request):
    return Response("<p1> This is the room sub url </p1>")

@api_view(['GET'])
def getUsers(request):
    users = UInfo.objects.all() #Query set of python objects (data needs to be serialized - turned into json format)
    serializer = UInfoSerializer(users, many=True) #returns a query set
    return Response(serializer.data) #displays all model data for User Info

@api_view(['GET'])
def getUser(request, primary_key): #To get one User instead of all like above ^^^
    #I added this if statement to practice
    if int(primary_key) > UInfo.objects.count() or not int(primary_key): #Use Django's built in count instead of len (it's better)
        return Response('Sorry ID out of range')
    
    users = UInfo.objects.get(id=primary_key)
    serializer = UInfoSerializer(users, many=False) #Many = False, serializes one single object
    return Response(serializer.data)