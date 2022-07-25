from django.shortcuts import render, HttpResponse
from .models import CpuTeam
from .forms import CpuTeamForm

# Create your views here.

# request가 들어오면 HTTPResponse()를 return


def index(request):
    number = 10

    return render(request, 'index.html', {"my_num": number})
    # return HttpResponse("<h1>Hello this is index View!</h1> (HTTP Response by django from webprogectApp/views.py)")


def CpuTeamModel_views(request):
    CpuTeam_All = CpuTeam.objects.all()
    # 만약 request가 POST 라면,
    # POST를 바탕으로 form을 완성하고
    # form이 유효하면 데이터를 저장
    if request.method == "POST":
        form = CpuTeamForm(request.POST)
        if form.is_valid():
            form.save()

    CpuTeamForm_All = CpuTeamForm()
    return render(request, 'CpuTeam.html', {"cputeam_list": CpuTeam_All, "CpuTeamForm": CpuTeamForm_All})
