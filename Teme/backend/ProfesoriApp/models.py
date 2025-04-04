from django.db import models
from AnUnivApp.models import AnUniversitar
from rest_framework import serializers

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
    an_universitar=models.ManyToManyField(AnUniversitar)
    salary=models.FloatField(null=False, blank=False, default=4000)

    def __str__(self):
        return self.email

class Create_Profesor_request(serializers.Serializer):
    nume=serializers.CharField()
    email=serializers.CharField()
    departament=serializers.CharField()
    salary=serializers.FloatField()
    an_universitar=serializers.ListField()

class Profesor_serializer(serializers.ModelSerializer):
    class Meta:
        model=Profesori
        fields="__all__"
