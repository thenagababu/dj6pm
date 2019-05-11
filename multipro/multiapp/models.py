from django.db import models


class customer(models.Model):
    cid=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)

class Emp(models.Model):
    eid = models.AutoField(primary_key=True)
    ename=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
class student(models.Model):
    sid = models.AutoField(primary_key=True)
    sname=models.CharField(max_length=50)
    fee=models.IntegerField()

class trainer(customer,Emp,student):
    tname=models.CharField(max_length=100)
    sal=models.IntegerField()
