from django.urls import path
from . import views #alternative 'from .views import *
#from .views import UInfoView

urlpatterns = [
    path('', views.home, name="home"),
    path('room/', views.room, name="room"),
    path('users/', views.getUsers, name="users"),
    path('users/<str:primary_key>/', views.getUser, name="user"), 
]