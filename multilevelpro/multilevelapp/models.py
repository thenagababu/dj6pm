from django.db import models

class customer(models.Model):
    cname=models.CharField(max_length=50)
    loc=models.CharField(max_length=50)

class Emp(customer):
    ename=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
class student(Emp):
    sname=models.CharField(max_length=50)
    fee=models.IntegerField()
