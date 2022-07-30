from django.urls import path
from . import views #alternative 'from .views import *
#from .views import UInfoView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('', views.home, name="home"),
    # path('room/', views.room, name="room"),
    # path('users/', views.getUsers, name="users"),
    # path('users/<str:primary_key>/', views.getUser, name="user"), 
]