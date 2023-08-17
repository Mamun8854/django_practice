from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    mobile = models.IntegerField(default=0)
