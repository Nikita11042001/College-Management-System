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
from django.urls import include, path

from . import result_urls, result_views, staff_views, student_urls, views

urlpatterns = [
   path('',views.index,name='index'),
   path('reports',views.reports,name='reports'),
   path('detaildoj',views.detaildoj,name='detaildoj'),
    path('detaildoa',views.detaildoa,name='detaildoa'),
    path('detailclass',views.detailclass,name='detailclass'),
    path('detailmarks',views.detailmarks,name='detailmarks'),
    path('detail1/<str:registrationno_1>/',views.detail1,name='detail1'),
   path('loginpage/',views.loginpage,name="loginpage"),
   path('dologin/',views.dologin,name='dologin'),
   path('logoutpage/',views.logoutpage,name='logoutpage'),
   path('registered/',views.registered,name='registered'),
   path('one/',views.one,name='one'),
   path('',include('case2.staff_urls')),
   path('',include('case2.student_urls')),
   path('',include('case2.result_urls')),
]
