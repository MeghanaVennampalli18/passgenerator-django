from django.urls import path
from app2.views import *
urlpatterns = [
    path('',home,name='home'),
    path('about',about,name='about'),
    path('generatepasswd',generatepasswd,name='password'),
    
]