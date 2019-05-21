from django.db import models
from multiselectfield import MultiSelectField
class EnquiryData(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=100)

    COURSES_CHOICES = (
        ('Py','Python'),
        ('Dj','Django'),
        ('API','REST API'),
        ('UI','UI')
    )
    courses = MultiSelectField(max_length=200,choices=COURSES_CHOICES)

    LOCATION_CHOICES = (
        ('Hyd','Hyderabad'),
        ('Bang','Bangalore'),
        ('Che','Chennai'),
        ('Pune','Pune')
    )
    locations = MultiSelectField(max_length=200, choices=LOCATION_CHOICES)

    SHIFT_CHOICES = (
        ('Morg','Morning'),
        ('Aftn','AfterNoon'),
        ('Evng','Evening'),
        ('Ngt','Night')
    )
    shifts = MultiSelectField(max_length=200,choices=SHIFT_CHOICES)

    gender = models.CharField(max_length=100)
    batch_start_date = models.DateField(max_length=100)