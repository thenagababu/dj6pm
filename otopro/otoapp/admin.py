from django.contrib import admin
from.models import student,course

class Adminstudent(admin.ModelAdmin):
    list_display = ['sname','sloc','email']

class Admincourse(admin.ModelAdmin):
    list_display = ['student','cname','cfee','institute']

admin.site.register(student,Adminstudent)
admin.site.register(course,Admincourse)