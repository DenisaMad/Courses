from django.db import models
from AnUnivApp.models import AnUniversitar

# Create your models here.

class Profesori(models.Model):
    DEPARTAMENT_CHOICES = [
        ('IT', 'IT'),
        ('M', 'Medicina'),
        ('L', 'Litere'),
        ('D','Drept'),
    ]
    nume=models.CharField(null=False , blank=False, unique=True,max_length=30)
    email=models.CharField(null=False , blank=False, unique=True,max_length=50)
    departament=models.CharField(null=False , blank=False,choices=DEPARTAMENT_CHOICES, max_length=30)
    an_universitae=models.ManyToManyField(AnUniversitar)

    def __str__(self):
        return self.email
