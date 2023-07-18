from django import forms

from .models import Result, Staff, Student, Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['name']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name','email','gender','address','contactno','DOB','DOJ','qualification','department','jobtitle','basicpay']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['registrationno','name','rollno','gender','address','parentcontactno','DOB','DOA','classname','Section']

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['registrationno','subjectname','marksobtained','passmarks','maximummarks','result']
