from django.db import models

# Create your models here.


class Departments(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    department = models.CharField(max_length=100)
    dateOfJoin = models.DateField()
    photoFileName = models.CharField(max_length=500);