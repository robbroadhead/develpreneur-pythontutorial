"""dpproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dpproject import views
from django.views.generic import TemplateView
from django.conf.urls import include


urlpatterns = [
    path('', views.HomePage),
    path('home2', TemplateView.as_view(template_name="homePage.html")),
    path('about2', TemplateView.as_view(template_name="aboutPage.html")),
    path('about', views.AboutPage),
    path('admin/', admin.site.urls),
    path('sum/<int:x>/<int:y>', views.AddPage),
    path('loop/<str:value>/<int:loop>', views.Looper),
    path('web', views.ShowPage),
    path('task/<int:id>', views.EditTask),
    path('task', views.CreateTask),
    path('tasks', views.ListTasks),
    path('web2', views.Examples),
    path('register/', views.userRegister),
    path('dbtest', views.showname),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', TemplateView.as_view(template_name="homePage.html")),
]
