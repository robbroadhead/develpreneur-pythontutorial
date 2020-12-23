from django.db import models
from django.contrib.auth.models import User
import datetime

class lkpStatus(models.Model):
    name = models.CharField(max_length=20,blank=False)
    shortname = models.CharField(max_length=4,blank=False)
    
    def __str__(self):
        return self.name
    
class Task(models.Model):
    name = models.CharField(max_length=50,blank=True,verbose_name="Name",help_text="Name of the task")
    duedate = models.DateTimeField(null=True,blank=True,verbose_name="Date Due")
    completiondate = models.DateTimeField(null=True,blank=True,verbose_name="Completed Date")
    status = models.ForeignKey(lkpStatus, on_delete=models.CASCADE,verbose_name="Status",db_index=True)
    attachment = models.FileField(null=True,blank=True)
    minutes_spent = models.IntegerField(null=True,blank=True,verbose_name="Time Spent",help_text="Minutes spent working this task",default=0)
    creationdate = models.DateTimeField(default=datetime.datetime.now,verbose_name="Created")
    owner = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Owner")

    def __str__(self):
        return self.name + "(" +  self.status.shortname + ")"
