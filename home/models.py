from django.db import models
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 100),
    age = models.IntegerField(),
    contact = models.IntegerField(),
    email = models.EmailField(),
    address = models.TextField(),

class tiger_park(models.Model):
    name = models.CharField(max_length=100),
    total_eployee = models.IntegerField(),
    clients = models.TextField()