from django.db import models
class RegistrationData():

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=100)

