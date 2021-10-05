from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.db.models import Q, QuerySet, query
from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                              get_object_or_404, redirect, render)

from .forms import ResultForm, StaffForm, StudentForm, TopicForm
from .models import Result, Staff, Student, Topic


@login_required
def resultdetails(request):
    return render(request,'result_templates/resultdetails.html')

@login_required
def results(request):
    results = Result.objects.all()
    students= Student.objects.all()
    context={'results': results,'students':students}
    return render(request,'result_templates/results.html',context)

@login_required
def add_subject(request):
    if request.method!='POST':
        form = ResultForm()
    else:
        form = ResultForm(data=request.POST)
        if form.is_valid():
            add_sub=form.save(commit=False)
            add_sub.owner= request.user
            add_sub.save()
            return redirect('results')
    context = {'form':form}
    return render(request,'result_templates/addsubject.html',context)

@login_required
def edit_subject(request, k_id):
    student = get_object_or_404(Result, subjectname=k_id)
    if request.method =='POST':
        form = ResultForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('results')
    context = {'form': ResultForm(instance=student)}
    return render(request,'result_templates/edit_subject.html', context)

@login_required
def search_result(request):
    if request.method=='POST':
        qur=request.POST['search']
        if qur:
            students= Student.objects.all()
            results = Result.objects.filter(Q(subjectname__icontains=qur ) |
                                        Q(registrationno = qur) 
                                        )
            if results:
                return render(request,'result_templates/search_result.html',{'results':results,'students':students})
            else:
                messages.error(request,'no results found')
        else:
            HttpResponseRedirect('/search_result/')
    return render(request,'result_templates/search_result.html')
