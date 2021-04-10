from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student, User, Course, Room

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #keeps config in one place. It tells the model effected by it is user model.
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)