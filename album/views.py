from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>Hello World!</h1>")
