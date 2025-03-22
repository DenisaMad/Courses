from django.db import models
from TaskApp.models import Task

# Create your models here.

class Profile(models.Model):
    email=models.CharField(null=False, blank=False,unique=True, max_length=50)
    password=models.CharField(null=False, blank=False, max_length=50)
    image=models.TextField(null=True, blank=True)
    tasks=models.ManyToManyField(Task, null=True, blank=True)