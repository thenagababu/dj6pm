from django.db import models

class Empdata(models.Model):
    ename=models.CharField(max_length=100)
    sal=models.IntegerField()
    email=models.EmailField()
    loc=models.CharField(max_length=100)
