from django.contrib import admin

from .models import Result, Staff, Student, Topic

# Register your models here.
admin.site.register(Topic)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Result)
