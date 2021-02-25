from django import forms
class RegisterForm(forms.Form):
    name = forms.CharField(label='真实名字:', max_length=25, min_length=2)   
    telephone = forms.IntegerField(label='手机号:', max_length = 11)
    password = forms.CharField(label="密码:", max_length=15, min_length=8)
    