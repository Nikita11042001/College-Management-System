"""case1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from . import staff_views, student_views, views

urlpatterns = [
    path('search_student/',student_views.search_student,name='search_student'),
    path('add_student/',student_views.add_student,name='add_student'),
    path('edit_student/<int:student_id>/',student_views.edit_student,name='edit_student'),
    path('topic1/<int:topic_id>/',student_views.topic1,name='topic1'),
    path('studentdetails/',student_views.studentdetails,name='studentdetails'),
    path('students/',student_views.students,name='students'),
]
