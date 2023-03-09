from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def Data(request):
    return  HttpResponse('<h1>hello world..!</h1>')
def Index(request):
    return render(request,'index.html')
