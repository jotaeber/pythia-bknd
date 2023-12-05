from django.db import models

# Create your models here.
class Student(models.Model):
    
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birth_date = models.DateField(null=True)
    course = models.CharField(max_length=50)
    ssn = models.DecimalField(max_digits=10, decimal_places=0)
    email = models.EmailField(max_length=200)
