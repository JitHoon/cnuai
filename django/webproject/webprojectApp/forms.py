from django import forms
from .models import CpuTeam  # 정보를 갱신할 model 불러오기


class CpuTeamForm(forms.ModelForm):  # ModelForm을 상속받는 cpu form 생성
    class Meta:
        model = CpuTeam
        fields = ('name', 'studentID', 'cool')
