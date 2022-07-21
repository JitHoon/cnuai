from django.shortcuts import render, HttpResponse

# Create your views here.

# request가 들어오면 HTTPResponse()를 return


def index(request):
    return HttpResponse("<h1>Hello this is index View!</h1> (HTTP Response by django from webprogectApp/views.py)")
