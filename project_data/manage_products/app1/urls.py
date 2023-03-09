from django.urls import path
# from . import views as v
from .views import *


# urlpatterns = [
#     path('Login',v.Company_login,name='login') ,   
#     path('Registration',v.Company_regi,name='login')    
# ]

urlpatterns = [
    path('',Company_login,name='login') ,   
    path('Registration',Company_regi,name='regi'),  
    path('Dashboard',Comdashboard,name='dash')    
]