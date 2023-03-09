from django.urls import path
from app1.views import Index_DAta

urlpatterns = [
path('Data/',Index_DAta)
]