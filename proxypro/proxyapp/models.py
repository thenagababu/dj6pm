from  django.db import models

class student(models.Model):
    student_number=models.IntegerField()
    student_name = models.CharField(max_length=50)
    student_location = models.CharField(max_length=50)
    student_email= models.EmailField(max_length=50)
class student_proxy(student):
    class Meta:
        proxy=True

