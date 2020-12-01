from django.contrib import admin
from dpproject.models import Task, lkpStatus

class TaskAdmin(admin.ModelAdmin):
    list_display=['name','duedate','status','owner']

class StatusAdmin(admin.ModelAdmin):
    list_display=['name','shortname']

admin.site.register(Task,TaskAdmin)
admin.site.register(lkpStatus,StatusAdmin)