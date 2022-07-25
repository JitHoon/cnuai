from django.shortcuts import render, HttpResponse
from .models import CpuTeam

# Create your views here.

# request가 들어오면 HTTPResponse()를 return


def index(request):
    number = 10

    return render(request, 'index.html', {"my_num": number})
    # return HttpResponse("<h1>Hello this is index View!</h1> (HTTP Response by django from webprogectApp/views.py)")


def CpuTeamModel_views(request):
    CpuTeam_All = CpuTeam.objects.all()
    return render(request, 'CpuTeam.html', {"cputeam_list": CpuTeam_All})
