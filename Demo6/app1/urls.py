from app1.views import Data
from django.urls import path
from app1.views import Index

urlpatterns = [
     path('Data/',Data),
    path('',Index),
   ]