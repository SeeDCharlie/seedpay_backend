
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from .views import *



urlpatterns = [
    #path('', include(router.urls) ),
    path('token-auth/', GenerateToken.as_view() ),
    path('logout/', logOut , name='logout'),
]