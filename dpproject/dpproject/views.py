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
    if not request.user.is_authenticated:
        return redirect('/accounts/login')

    return redirect('/todo')

def AboutPage(request):
    msg = ""
    parms = {"msg": msg}
    return render(request,'aboutPage.html',parms)
    
def Looper(request,value,loop):
    for i in range(loop):
        print(value)

    return HttpResponse("Success")

def completeTask(request,id):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')

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
    if not request.user.is_authenticated:
        return redirect('/accounts/login')

    data = Task()
    data.owner = request.user
    parent = Timeframe()
    if 'p' in request.session:
        pid = request.session['p']
        tf = Timeframe.objects.get(pk=pid)
        data.timeframe = tf
        parent = tf

    msg = "Create a New Record"
    title = "Create Task"
    if request.method == "POST":
        form = forms.TaskForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            msg = "Record Saved"
        else:
            msg = "Invalid Record"
            
    form = forms.TaskForm(instance=data)
    parms = {"form": form, "title": title, "msg": msg, "parent": parent}
    return render(request,'TaskEdit.html',parms)

def deleteTasks(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')

    Task.objects.all().delete()
    tasks = Task.objects.all()
    title = "All Tasks"
    parms = {"title": title, "tasks": tasks}
    return render(request,'TaskList.html',parms)

def massUpdate(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')

    Task.objects.filter(minutes_spent == 0 ).update(minutes_spent = 2)
    tasks = Task.objects.all()
    title = "All Tasks"
    parms = {"title": title, "tasks": tasks}
    return render(request,'TaskList.html',parms)

def EditTask(request,id):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')

    data = Task.objects.get(pk=id)
    data.owner = request.user
    form = forms.TaskForm(instance=data)
    parent = data.timeframe
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

    if 'p' in request.session:
        pid = request.session['p']
        parent = Timeframe.objects.get(pk=pid)
        data.parent = parent

    title = "Edit Task"
    parms = {"form": form, "title": title, "msg": msg, "parent": parent}
    return render(request,'TaskEdit.html',parms)

def ListTasks(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')

    tasks = Task.objects.all().order_by('duedate','name')
    title = "All Tasks"
    parms = {"title": title, "tasks": tasks}
    return render(request,'TaskList.html',parms)

def ListRoadmaps(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')

    items = Roadmap.objects.raw('select rmp.id,rmp.name,rmp.startdate,count(tf.id) as timeframes,0 as minutes from dpproject_roadmap rmp left join dpproject_timeframe tf on rmp.id = tf.roadmap_id group by rmp.id')
    title = "My Roadmaps"
    parms = {"title": title, "items": items}
    return render(request,'RoadmapList.html',parms)

def cleanSession(request):
    request.session['rmid'] = None
    request.session['p'] = None
    
def CreateRoadmap(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    
    cleanSession(request)
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
    if not request.user.is_authenticated:
        return redirect('/accounts/login')

    request.session['rmid'] = id
    request.session['p'] = None
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
    tfs = Timeframe.objects.filter(roadmap=data,parent__isnull=True).order_by('name')
    parms = {"form": form, "title": title, "msg": msg, "timeframes": tfs, "rmid": id}
    return render(request,'RoadmapEdit.html',parms)

def ActiveTasks(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')

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
    if not request.user.is_authenticated:
        return redirect('/accounts/login')

    data = Timeframe.objects.get(pk=id)
    form = forms.TimeframeForm(instance=data)
    roadmap = []
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

    if 'rmid' in request.session:
        rid = request.session['rmid']
        roadmap = Roadmap.objects.get(pk=rid)

    title = "Edit Time Frame"
    tasks = Task.objects.filter(timeframe=data).order_by('duedate','name')
    children = Timeframe.objects.filter(parent=data)
    parent = data.parent

    request.session['p'] = id
    parms = {"form": form, "title": title, "msg": msg, "tasks": tasks, "tfid": id, "roadmap": roadmap, "children": children, "parent": parent, 'rmid': roadmap.id}
    return render(request,'TimeframeEdit.html',parms)

def ListTimeframes(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')

    tfs = Timeframe.objects.all().order_by('name')
    title = "All Time Frames"
    parms = {"title": title, "timeframes": tfs}
    return render(request,'TimeframeList.html',parms)

def CreateTimeframe(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')

    data = Timeframe()
    if 'rmid' in request.session:
        rid = request.session['rmid']
        roadm = Roadmap.objects.get(pk=rid)
        data.roadmap = roadm
    if 'p' in request.session:
        pid = request.session['p']
        if pid != None:
            parent = Timeframe.objects.get(pk=pid)
            data.parent = parent

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
    parms = {"form": form, "title": title, "msg": msg, "tfid": id}
    return render(request,'TimeframeEdit.html',parms)
