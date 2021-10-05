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
from django.contrib import admin
from django.urls import path

from . import staff_views, views

urlpatterns = [
   path('topics/',staff_views.topics,name='topics'),
   path('topic/<int:topic_id>/',staff_views.topic,name='topic'),
   path('search/',staff_views.search,name='search'),
   path('staffs/',staff_views.staffs,name="staffs"),
   path('staffdetails/',staff_views.staffdetails,name="staffdetails"),
   path('add_staff/<int:topic_id>/',staff_views.add_staff,name='add_staff'),
   path('add_newstaff/',staff_views.add_newstaff,name='add_newstaff'),
   path('edit_staff/<int:staff_id>/',staff_views.edit_staff,name='edit_staff'),
]
