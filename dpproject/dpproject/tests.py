from django.test import Client,TestCase
from django.db import models
from dpproject.models import lkpStatus, Task
from django.contrib.auth.models import User

class AllTests(TestCase):
    TestName = "Not Defined"
    c = Client()

    def setUp(self):
        status = lkpStatus()
        status.name = "Complete"
        status.shortname = "COMP"
        status.save()
        status = lkpStatus()
        status.name = "Cancel"
        status.shortname = "CNCL"
        status.save()
        
    def test1(self):
        items = lkpStatus.objects.all()
        self.assertEqual(len(items),2)
        
        self.assertEqual(self.TestName,"Not Defined")
        self.TestName = "Test One"
        self.assertEqual(self.TestName,"Test One")
        
    def test2(self):
        items = lkpStatus.objects.all()
        self.assertEqual(len(items),2)

        item = lkpStatus.objects.get(shortname="COMP")
        item.name = "Completed"
        item.save()
        self.assertEqual(item.name,"Completed")

    def test3(self):
        item = lkpStatus.objects.get(shortname="COMP")
        self.assertEqual(item.name,"Complete")

    def test4(self):
        response = self.c.get('/')
        # print(response.status_code)

    def test5(self):
        response = self.c.get('/web')
        # print(response.status_code)
        # print(response)

    def test6(self):
        user = User.objects.create_user(username='Tester',password='qwerty123')
        user.save()
        task = Task()
        task.name = "Item 1"
        task.status = lkpStatus.objects.get(shortname='COMP')
        task.owner = user
        task.save()

        login = self.c.login(username='Tester',password='qwerty123')
        self.assertEqual(login,True)

        response = self.c.get('/tasks')
        self.assertEqual(response.status_code,200)

#    path('', views.HomePage),
#   path('home2', TemplateView.as_view(template_name="homePage.html")),
#    path('about2', TemplateView.as_view(template_name="aboutPage.html")),
#   path('about', views.AboutPage),
#    path('admin/', admin.site.urls),
#    path('sum/<int:x>/<int:y>', views.AddPage),
#   path('loop/<str:value>/<int:loop>', views.Looper),
#   path('web', views.ShowPage),
#   path('task/<int:id>', views.EditTask),
#    path('task', views.CreateTask),
#   path('complete/<int:id>', views.completeTask),
#   path('tasks', views.ListTasks),
#   path('todo', views.ActiveTasks),
#   path('web2', views.Examples),
