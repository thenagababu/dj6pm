from django.db import models

class student(models.Model):
    sname=models.CharField(max_length=50)
    sloc=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)

    def __str__(self):
        return self.sname

class course(models.Model):
    student=models.ForeignKey(student)
    cname=models.CharField(max_length=50)
    cfee=models.IntegerField()
    institute= models.CharField(max_length=50)

    def __str__(self):
        return self.cname


