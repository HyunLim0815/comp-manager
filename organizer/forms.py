from django import forms
from django.utils import timezone

class PerfectINFO(forms.Form):
    name = forms.CharField(max_length=25, min_length=2, label="组织名字")
    introduction = forms.CharField(min_length=50, max_length=200, label="组织简介")
    telephone = forms.IntegerField(label='联系人手机号')
    
class ComForm(forms.Form):
    name = forms.CharField()
    types = forms.CharField()
    start = forms.DateField()
    end = forms.DateField()
    status = forms.CharField(max_length=5)
    rules = forms.CharField(max_length=1500)