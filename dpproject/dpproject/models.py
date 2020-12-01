from django.db import models
from django.contrib.auth.models import User
import datetime

class lkpStatus(models.Model):
    name = models.CharField(max_length=20,blank=False)
    shortname = models.CharField(max_length=4,blank=False)
    
    def __str__(self):
        return self.name
    
class Task(models.Model):
    name = models.CharField(max_length=50,blank=True)
    duedate = models.DateTimeField(null=True,blank=True)
    completiondate = models.DateTimeField(null=True,blank=True)
    status = models.ForeignKey(lkpStatus, on_delete=models.CASCADE)
    minutes_spent = models.IntegerField(null=True,blank=True)
    creationdate = models.DateTimeField(default=datetime.datetime.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + "(" +  self.status.shortname + ")"
