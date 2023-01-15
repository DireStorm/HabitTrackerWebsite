from django.urls import path
from . import views #alternative 'from .views import *
from .views import MyTokenObtainPairView
from .api import RegisterApi
#from .views import UInfoView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes),
    # path('habits/', views.getHabits),
    
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterApi.as_view()),
    path('profiles/', views.profile_list),
    path('profiles/<int:pk>/', views.profile_details),
    
    # path('', views.home, name="home"),
    # path('room/', views.room, name="room"),
    # path('users/', views.getUsers, name="users"),
    #path('users/<str:primary_key>/', views.getUser, name="user"), 
]