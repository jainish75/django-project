from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Records(req):
    return  HttpResponse('<h1>app2</h1>')