from . import models
from django import forms
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ["name","duedate","completiondate","status","minutes_spent","owner","creationdate"]
        widgets = {
            "name" : forms.TextInput(attrs={'size':50,'class' : 'textInput'}),
            "completiondate" : forms.SelectDateWidget(),
            "duedate" : forms.SelectDateWidget(),
            "owner" : forms.HiddenInput(),
            "creationdate" : forms.HiddenInput()
        }

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.CharField(max_length=40)
    lastname = forms.CharField(max_length=40)
    
    class Meta:
        model = User
        fields = ['username','firstname','lastname','email','password1','password2']