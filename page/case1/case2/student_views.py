from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.db.models import Q, QuerySet, query
from django.shortcuts import (HttpResponseRedirect, get_object_or_404,
                              redirect, render)

from .forms import StaffForm, StudentForm, TopicForm
from .models import Staff, Student, Topic


@login_required
def studentdetails(request):
    return render(request,'student_templates/studentdetails.html')

@login_required
def add_student(request):
    if request.method!='POST':
        form = StudentForm()
    else:
        form = StudentForm(data=request.POST)
        if form.is_valid():
            new_stu=form.save(commit=False)
            new_stu.owner= request.user
            new_stu.save()
            return redirect('students')
    context = {'form':form}
    return render(request,'student_templates/add_student.html',context)

@login_required
def topic1(request,topic_id):
    topic1=Student.objects.get(id=topic_id)
    Students= Student.objects.filter(id=topic_id)
    context={'topic1':topic1,'Students':Students}
    return render(request,'student_templates/t.html',context)

@login_required
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method =='POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('topic1',topic_id=student_id)
    context = {'form': StudentForm(instance=student)}
    return render(request,'student_templates/edit_student.html', context)

@login_required
def students(request):
    students = Student.objects.all()
    context={'students': students}
    return render(request,'student_templates/s.html',context)

@login_required
def search_student(request):
    if request.method=='POST':
        qur=request.POST['search']
        if qur:
            Students = Student.objects.filter(Q(rollno__icontains= qur) |
                                        Q(name__icontains=qur ) |
                                        Q(registrationno = qur) |
                                        Q(parentcontactno__icontains= qur))
            if Students:
                return render(request,'student_templates/search1.html',{'Students':Students})
            else:
                messages.error(request,'no details found')
        else:
            HttpResponseRedirect('/search_student/')
    return render(request,'student_templates/search1.html')
