from .views import *
from django.urls import path
from app1.views import NewData
urlpatterns = [
    path('Data/',NewData,name='cals'),
    path('',Index,name='home'),
    path('About_Us/',About_Us,name='about'),
    path('Blog/',Blog,name='blog'),
    path('Contact_Us/',Contact_Us,name='contact'),
   ]
#    name use in index.html link=...
