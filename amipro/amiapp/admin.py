from django.contrib import admin
from.models import Customer,Emp,Student

class AdminCustomer(admin.ModelAdmin):
    list_display = ['cname','loc','email']

class AdminEmp(admin.ModelAdmin):
    list_display = ['cname','loc','email']

class AdminStudent(admin.ModelAdmin):
    list_display = ['cname','loc','email']

admin.site.register(Student,AdminStudent)
admin.site.register(Emp,AdminStudent)
admin.site.register(Customer,AdminStudent)