from django import forms
from django.forms import ModelForm
from .models import Users
class LoginForm(ModelForm):
    class Meta:
        model = Users
        fields = [
            'telephone', 'password', 'email'
        ]