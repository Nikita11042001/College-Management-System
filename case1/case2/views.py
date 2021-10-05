from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.db.models import DecimalField, F, FloatField, IntegerField, Sum
from django.http import Http404
from django.shortcuts import (HttpResponse, HttpResponseRedirect, redirect,
                              render)

from .forms import ResultForm, StaffForm, StudentForm, TopicForm
from .models import Result, Staff, Student, Topic

# Create your views here.

def loginpage(request):
    return render(request,"login1.html")

def dologin(request):    
    if request.method!='POST':
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user!=None:
            login(request,user)
            return HttpResponseRedirect('/one')
         
        else:
            return redirect('/')


def index(request):
    return render(request,'staff_templates/index.html')

def logoutpage(request):
    return render(request,'staff_templates/log_out.html')

def registered(request):
    return render(request,'staff_templates/registered.html')

@login_required
def one(request):
    if request.user.is_superuser:
        return render(request,'staff_templates/onepagemore.html')
    else:
        return render(request,'staff_templates/staffaccess.html')


@login_required
def reports(request):
    return render(request,'reports.html')

@login_required
def detaildoj(request):
    staff= Staff.objects.order_by('DOJ')
    return render(request,'detaildoj.html',{'sr':staff})

@login_required
def detaildoa(request):
    staff= Student.objects.order_by('DOA')
    return render(request,'detaildoa.html',{'Students':staff})

@login_required
def detailclass(request):
    staff= Student.objects.order_by('DOA')
    return render(request,'detailclass.html',{'Students':staff})

@login_required
def detailmarks(request):
    results = Result.objects.all()
    students= Student.objects.all()
    context={'results': results,'students':students}
    return render(request,'detailmarks.html',context)

def detail1(request,registrationno_1):
    sum=Result.objects.filter(registrationno=registrationno_1).aggregate(
        Student_Marks=Sum('marksobtained'),
        Total_Marks=Sum('maximummarks')
        )
    sum1=Result.objects.filter(registrationno=registrationno_1).aggregate(
        Total_Percentage=Sum('marksobtained')*100/Sum('maximummarks'))
    s=sum1.get('Total_Percentage')
    detail1=Student.objects.get(registrationno=registrationno_1)
    results = Result.objects.filter(registrationno=registrationno_1)
    students= Student.objects.filter(registrationno=registrationno_1)
    context={'results': results,'students':students,'sum':sum,'sum1':sum1}
    return render(request,'detail1.html',context)
