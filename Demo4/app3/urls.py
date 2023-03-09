from django.urls import path
from app3.views import Database

urlpatterns = [
path('database/',Database)
]