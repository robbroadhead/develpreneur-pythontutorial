from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from dpproject.models import Task,lkpStatus,Roadmap,Timeframe
import mysql
from mysql.connector import Error
from django.db.models import Q

def AddPage(request,x,y):
    return HttpResponse(x + y);
    
def HomePage(request):
    return redirect('/accounts/login')
    
def AboutPage(request):
    msg = ""
    parms = {"msg": msg}
    return render(request,'aboutPage.html',parms)
    
def Looper(request,value,loop):
    for i in range(loop):
        print(value)

    return HttpResponse("Success")

def completeTask(request,id):
    complete = lkpStatus.objects.get(pk=3)
    print(complete)
    task = Task.objects.get(pk=id)
    task.status = complete
    task.save()
    print("Task " + str(id) + " is complete.")
    return HttpResponse("Success")
    
def ShowPage(request):
    return render(request,'default.html')

def userRegister(request):
    form = forms.RegistrationForm()
    params = {"form": form}
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    
    return render(request,'register.html',params)

def CreateTask(request):
    data = Task()
    data.owner = request.user
    form = forms.TaskForm(instance=data)
    msg = "Create a New Record"
    title = "Create Task"
    if request.method == "POST":
        form = forms.TaskForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            msg = "Record Saved"
        else:
            msg = "Invalid Record"
    parms = {"form": form, "title": title, "msg": msg}
    return render(request,'TaskEdit.html',parms)

def deleteTasks(request):
    Task.objects.all().delete()
    tasks = Task.objects.all()
    title = "All Tasks"
    parms = {"title": title, "tasks": tasks}
    return render(request,'TaskList.html',parms)

def test(request):
    # status = lkpStatus.objects.get(shortname="NEW")
    # Task.objects.create(name="Task 3",status=status, owner=request.user)
    # Task.objects.create(name="Task 4",status=status, owner=request.user)
    # Task.objects.create(name="Task 5",status=status, owner=request.user)
    # Task.objects.create(name="Task 6",status=status, owner=request.user)
    # Task.objects.create(name="Task 7",status=status, owner=request.user)

    # Display results
    tasks = Task.objects.exclude(name__contains='7')
    # tasks = Task.objects.filter(name__contains='ask')[:5]
    # tasks = Task.objects.exclude(name__contains='Task')
    # tasks = Task.objects.raw('select * from dpproject_task group by name')
    title = "All Tasks"
    parms = {"title": title, "tasks": tasks}
    return render(request,'TaskList.html',parms)

def massUpdate(request):
    Task.objects.filter(minutes_spent == 0 ).update(minutes_spent = 2)
    tasks = Task.objects.all()
    title = "All Tasks"
    parms = {"title": title, "tasks": tasks}
    return render(request,'TaskList.html',parms)

def EditTask(request,id):
    data = Task.objects.get(pk=id)
    data.owner = request.user
    form = forms.TaskForm(instance=data)
    msg = "Please update data for the record"
    if request.method == "POST":
        if 'delete' in request.POST:
            data = Task.objects.get(pk=id).delete()
            msg = "Record Deleted"
            return redirect('/tasks')
        else: 
            form = forms.TaskForm(request.POST, instance=data)
            if form.is_valid():
                form.save()
                msg = "Record Saved"
                return redirect('/tasks')
            else:
                msg = "Invalid Record"
    title = "Edit Task"
    parms = {"form": form, "title": title, "msg": msg}
    return render(request,'TaskEdit.html',parms)

def ListTasks(request):
    tasks = Task.objects.all().order_by('duedate','name')
    title = "All Tasks"
    parms = {"title": title, "tasks": tasks}
    return render(request,'TaskList.html',parms)

def ListRoadmaps(request):
    items = Roadmap.objects.all().order_by('name')
    title = "My Roadmaps"
    parms = {"title": title, "items": items}
    return render(request,'RoadmapList.html',parms)

def CreateRoadmap(request):
    data = Roadmap()
    data.owner = request.user
    form = forms.RoadmapForm(instance=data)
    msg = "Create a New Record"
    title = "Create Roadmap"
    if request.method == "POST":
        form = forms.RoadmapForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            msg = "Record Saved"
        else:
            msg = "Invalid Record"
        return redirect("/roadmaps")

    parms = {"form": form, "title": title, "msg": msg}
    return render(request,'RoadmapEdit.html',parms)

def EditRoadmap(request,id):
    data = Roadmap.objects.get(pk=id)
    data.owner = request.user
    form = forms.RoadmapForm(instance=data)
    msg = "Please update data for the record"
    print(request.POST)
    if request.method == "POST":
        if 'delete' in request.POST:
            data = Roadmap.objects.get(pk=id).delete()
            msg = "Record Deleted"
            return redirect('/roadmaps')
        else: 
            form = forms.RoadmapForm(request.POST, instance=data)
            if form.is_valid():
                form.save()
                msg = "Record Saved"
                return redirect('/roadmaps')
            else:
                msg = "Invalid Record"
    title = "Edit Roadmap"
    tfs = Timeframe.objects.filter(roadmap=data).order_by('name')
    parms = {"form": form, "title": title, "msg": msg, "timeframes": tfs}
    return render(request,'RoadmapEdit.html',parms)

def ActiveTasks(request):
    cancel = lkpStatus.objects.get(shortname='CNCL')
    complete = lkpStatus.objects.get(shortname='COMP')
    tasks = Task.objects.filter(~Q(status=complete)).order_by('duedate','name')
    title = "Active Tasks"
    parms = {"title": title, "tasks": tasks}
    return render(request,'TaskList.html',parms)

def Examples(request):
    return redirect('/web')

def showname(request):
    config = {
        'user' : 'root',
        'password': 'develpreneur',
        'host': '127.0.0.1',
        'database': 'dpproject',
        'raise_on_warnings': True
    }
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    name = "Not Found"
    try:
        sql = "select first_name,last_name,email from auth_user"
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            print("Email Address is: {}".format(row[2]))
            name = row[1] + ", " + row[0]
    except Error as e:
        print(e)
    return HttpResponse(name)

def EditTimeframe(request,id):
    data = Timeframe.objects.get(pk=id)
    form = forms.TimeframeForm(instance=data)
    msg = "Please update data for the record"
    if request.method == "POST":
        if 'delete' in request.POST:
            data = Timeframe.objects.get(pk=id).delete()
            msg = "Record Deleted"
            return redirect('/tfs')
        else: 
            form = forms.TimeframeForm(request.POST, instance=data)
            if form.is_valid():
                form.save()
                msg = "Record Saved"
                return redirect('/tfs')
            else:
                msg = "Invalid Record"
    title = "Edit Time Frame"
    tasks = Task.objects.filter(timeframe=data).order_by('duedate','name')

    parms = {"form": form, "title": title, "msg": msg, "tasks": tasks}
    return render(request,'TimeframeEdit.html',parms)

def ListTimeframes(request):
    tfs = Timeframe.objects.all().order_by('name')
    title = "All Time Frames"
    parms = {"title": title, "timeframes": tfs}
    return render(request,'TimeframeList.html',parms)

def CreateTimeframe(request):
    data = Timeframe()
    form = forms.TimeframeForm(instance=data)
    msg = "Create a New Record"
    title = "Create Time Frame"
    if request.method == "POST":
        form = forms.TimeframeForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            msg = "Record Saved"
        else:
            msg = "Invalid Record"
    parms = {"form": form, "title": title, "msg": msg}
    return render(request,'TimeframeEdit.html',parms)

