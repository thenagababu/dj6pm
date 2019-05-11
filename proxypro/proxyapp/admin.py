from django.contrib import admin
from .models import student,student_proxy

class Adminstudent(admin.ModelAdmin):
    list_display = ['student_number','student_name','student_location','student_email']

class Adminstudent_proxy(admin.ModelAdmin):
    list_display = ['student_number','student_name','student_location','student_email']

admin.site.register(student,Adminstudent)
admin.site.register(student_proxy,Adminstudent_proxy)