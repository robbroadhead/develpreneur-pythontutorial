from . import models
from django import forms
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TimeframeForm(forms.ModelForm):
    class Meta:
        model = models.Timeframe
        fields = ["parent","name","roadmap","period"]
        widgets = {
            "name" : forms.TextInput(attrs={'size':50,'class' : 'textInput'}),
        }


class RoadmapForm(forms.ModelForm):
    class Meta:
        model = models.Roadmap
        fields = ["name","startdate","completiondate","owner","creationdate"]
        widgets = {
            "name" : forms.TextInput(attrs={'size':50,'class' : 'textInput'}),
            "completiondate" : forms.SelectDateWidget(),
            "startdate" : forms.SelectDateWidget(),
            "owner" : forms.HiddenInput(),
            "creationdate" : forms.HiddenInput()
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ["name","description","duedate","attachment","completiondate","status","minutes_spent","owner","creationdate","timeframe"]
        widgets = {
            "name" : forms.TextInput(attrs={'size':50,'class' : 'textInput'}),
            "description" : forms.Textarea(attrs={'cols':80,'rows':'5','class':'inputText'}),
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