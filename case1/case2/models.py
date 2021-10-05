from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Topic(models.Model):
    name=models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Staff(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=150)
    gender=models.CharField(max_length=100)
    address=models.TextField()
    contactno=models.IntegerField()
    DOJ=models.DateField()
    DOB=models.DateField()
    qualification=models.TextField(max_length=1000)
    department=models.CharField(max_length=100)
    jobtitle=models.CharField(max_length=100)
    basicpay=models.IntegerField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural='Staffs'

    def __str__(self):
        return self.name

class Student(models.Model):
    id=models.AutoField(primary_key=True)
    registrationno=models.CharField(max_length=10)
    rollno=models.IntegerField()
    name=models.CharField(max_length=200)
    gender=models.CharField(max_length=100)
    address=models.TextField()
    parentcontactno=models.IntegerField()
    DOA=models.DateField()
    DOB=models.DateField()
    classname=models.CharField(max_length=100)
    Section=models.CharField(max_length=100)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural='Students'

    def __str__(self):
        return self.name

class Result(models.Model):
    registrationno=models.CharField(max_length=10)
    subjectname=models.CharField(max_length=200)
    marksobtained=models.IntegerField()
    passmarks=models.IntegerField()
    maximummarks=models.IntegerField()
    result=models.CharField(max_length=10)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural='Results'
        
    def __str__(self):
        return self.registrationno
