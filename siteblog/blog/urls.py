from django.shortcuts import render
from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home')
]