from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app2_first(request):
    return HttpResponse('<h1>app2_first function</h2>')

def app2_second(request):
    return HttpResponse('<marquee><h1>app2_second function</h1></marqiuee>')