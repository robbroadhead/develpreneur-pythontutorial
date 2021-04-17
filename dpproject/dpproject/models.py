from django.db import models
from django.contrib.auth.models import User
import datetime

class lkpStatus(models.Model):
    name = models.CharField(max_length=20,blank=False)
    shortname = models.CharField(max_length=4,blank=False)
    
    def __str__(self):
        return self.name
    
class Roadmap(models.Model):
    name = models.CharField(max_length=50,blank=True,verbose_name="Name",help_text="Name of the roadmap")
    startdate = models.DateTimeField(null=True,blank=True,verbose_name="Date Due")
    completiondate = models.DateTimeField(null=True,blank=True,verbose_name="Completed Date")
    creationdate = models.DateTimeField(default=datetime.datetime.now,verbose_name="Created")
    owner = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Owner")

    def __str__(self):
        return self.name + "(" +  str(self.startdate) + ")"

class Timeframe(models.Model):
    PERIOD_CHOICES = [
        (0,"Annual"),
        (1,"Quarterly"),
        (2,"Monthly"),
        (3,"Weekly")
    ]
    name = models.CharField(max_length=50,blank=True,verbose_name="Name",help_text="Name of the timeframe")
    roadmap = models.ForeignKey(Roadmap, on_delete=models.CASCADE,verbose_name="Roadmap")
    parent = models.ForeignKey('self', on_delete=models.CASCADE,verbose_name="Parent",null=True,blank=True)
    period = models.IntegerField(choices=PERIOD_CHOICES,default=0)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=50,blank=True,verbose_name="Name",help_text="Name of the task")
    description = models.CharField(max_length=500,blank=True,verbose_name="Description",help_text="Details about the task")
    duedate = models.DateTimeField(null=True,blank=True,verbose_name="Date Due")
    completiondate = models.DateTimeField(null=True,blank=True,verbose_name="Completed Date")
    status = models.ForeignKey(lkpStatus, on_delete=models.CASCADE,verbose_name="Status",db_index=True)
    attachment = models.FileField(null=True,blank=True)
    minutes_spent = models.IntegerField(null=True,blank=True,verbose_name="Time Spent",help_text="Minutes spent working this task",default=0)
    creationdate = models.DateTimeField(default=datetime.datetime.now,verbose_name="Created")
    owner = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Owner")
    timeframe = models.ForeignKey(Timeframe, on_delete=models.CASCADE,verbose_name="Timeframe",null=True,blank=True)

    def __str__(self):
        return self.name + "(" +  self.status.shortname + ")"

