from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("rango says hey there partner!" + "<a href=http://127.0.0.1:8000/rango/about/>about page</a>")

def about(request):
    return HttpResponse("Rango says here is the about page." +"<a href=http://127.0.0.1:8000/>home page</a>")