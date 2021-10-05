from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.http.response import Http404
from django.shortcuts import (HttpResponseRedirect, get_object_or_404,
                              redirect, render)

from .forms import StaffForm, TopicForm
from .models import Staff, Topic


# Create your views here.
@login_required
def staffdetails(request):
    return render(request,'staff_templates/staffdetails.html')

@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request,'staff_templates/staffname.html',context)

@login_required
def topic(request,topic_id):
    topic= Topic.objects.get(id=topic_id)
    Staffs= Staff.objects.filter(id=topic_id)
    if topic.owner!= request.user:
        raise Http404
    context={'topic':topic,'Staffs':Staffs}
    return render(request,'staff_templates/topic.html',context)

@login_required
def add_newstaff(request):
    if request.method!='POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_staff=form.save(commit=False)
            new_staff.owner = request.user
            new_staff.save()
            return redirect('topics')
    context = {'form':form}
    return render(request,'staff_templates/add_newstaff.html',context)

@login_required
def add_staff(request,topic_id):
    topic=Topic.objects.get(id= topic_id)
    if request.method!='POST':
        form = StaffForm()
    else:
        form = StaffForm(data=request.POST)
        if form.is_valid():
            add_staff=form.save(commit=False)
            add_staff.owner= request.user
            add_staff.save()
            return redirect('one')
    context = {'topic':topic,'form':form}
    return render(request,'staff_templates/add_staff.html',context)

@login_required
def edit_staff(request,staff_id):
    staff=Staff.objects.get(id=staff_id)
    topic = staff.topic
    if topic.owner!= request.user:
        raise Http404
    if request.method!='POST':
        form=StaffForm(instance=staff)
    else:
        form=StaffForm(instance=staff,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('topic',topic_id=topic.id)
    context={'staff':staff,'topic':topic,'form':form}
    return render(request,'staff_templates/edit_staff.html',context)

@login_required
def staffs(request):
    if topic.owner!= request.user:
        raise Http404
    staffs = Staff.objects.all()
    context={'staffs': staffs}
    return render(request,'staff_templates/staffs.html',context)

def search(request):
     # Catch the data and search in Staff model.
    if request.method=='POST':
        srch1 = request.POST['srch']
        try:
            srch1 = int(srch1)
            if type(srch1)== int:
                match= Staff.objects.filter(id=srch1)
                if match :
                    return render(request,'staff_templates/search.html',{'sr': match})
                else:
                    messages.error(request,'no results,found')
            else:

                return HttpResponseRedirect("/search")
        except:
            catch= Staff.objects.filter(name=srch1)
            if catch:
                return render(request,'staff_templates/search.html',{'sr': catch})
            else:
                messages.error(request,'no results,found')
                return HttpResponseRedirect("/search")

    return render(request,"staff_templates/search.html")
