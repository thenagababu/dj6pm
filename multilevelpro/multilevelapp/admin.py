from django.contrib import admin
from .models import customer,Emp,student

class Admincustomer(admin.ModelAdmin):
    list_display = ['cname','loc']
class AdminEmp(admin.ModelAdmin):
    list_display = ['ename','email']
class Adminstudent(admin.ModelAdmin):
    list_display = ['sname','fee']
admin.site.register(customer,Admincustomer)
admin.site.register(Emp,AdminEmp)
admin.site.register(student,Adminstudent)