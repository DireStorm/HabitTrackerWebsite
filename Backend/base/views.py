#from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view #, permission_classes #decorator import
# from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# from .serializer import HabitSerializer
# from .models import Habit

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims for token
        token['username'] = user.username #token is an encrypted dict, so you are just adding a key-value pair for the username
        token['email'] = user.email #stores email in encrypted dict - I added this line

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# Create your views here.

#Function Based Views

#Method to store all end points
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)

# @api_view(['PUT'])
# # @permission_classes([IsAuthenticated]) #Creates a protected route, so have to be authenticated to access this info
# def getHabits(request):
#     user = request.user
#     habits = user.habit_set.all() #You will need Habit.objects.all() when creating the leaderboard
#     serializer = HabitSerializer(habits, many=True)
#     return Response(serializer.data)






#### Learning Stuff ############# - Will Delete Later!!!

# #These are just for practice (you typically don't want to create views - renderings - in the urls file)
# @api_view(['GET']) #Decorator for API  usability 
# def home(request):
#     return Response("<h1> Jerin's Website </h1>")

# @api_view(['GET'])
# def room(request):
#     return Response("<p1> This is the room sub url </p1>")

# @api_view(['GET'])
# def getUsers(request):
#     users = UInfo.objects.all() #Query set of python objects (data needs to be serialized - turned into json format)
#     serializer = UInfoSerializer(users, many=True) #returns a query set
#     return Response(serializer.data) #displays all model data for User Info

# @api_view(['GET'])
# def getUser(request, primary_key): #To get one User instead of all like above ^^^
#     #I added this if statement to practice
#     if int(primary_key) > UInfo.objects.count() or not int(primary_key): #Use Django's built in count instead of len (it's better)
#         return Response('Sorry ID out of range')
    
#     users = UInfo.objects.get(id=primary_key)
#     serializer = UInfoSerializer(users, many=False) #Many = False, serializes one single object
#     return Response(serializer.data)