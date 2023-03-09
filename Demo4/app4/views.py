from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Data(req):
    return HttpResponse('<h1>welcome to app4</h1>')