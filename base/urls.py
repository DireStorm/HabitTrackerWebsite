from django.urls import path
from . import views #alternative 'from .views import *

urlpatterns = [
    path('', views.home, name="home"),
    path('room/', views.room, name="room")
]