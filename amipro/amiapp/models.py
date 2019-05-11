from django.db import models

class commondata(models.Model):
    loc=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)

    class meta:
        abstract=True

class Customer(commondata):
    cname=models.CharField(max_length=50)

class Emp(commondata):
    cname=models.CharField(max_length=50)

class Student(commondata):
    cname=models.CharField(max_length=50)