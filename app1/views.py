from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app1_first(request):
    return HttpResponse('<h1>app1 first view function</h1>')

def app1_second(request):
    return HttpResponse('<marquee><h1>app1_second function</h1></marquee>')
