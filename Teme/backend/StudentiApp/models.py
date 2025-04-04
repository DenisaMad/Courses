from django.db import models
from ProfesoriApp.models import Profesori
from AnUnivApp.models import AnUniversitar
from rest_framework import serializers
# Create your models here.

class Student(models.Model):
    nume = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(unique=True, null=False, blank=False, max_length=50)
    an_universitar = models.ForeignKey(AnUniversitar,on_delete=models.CASCADE, null=False, blank=False) 
    tutore = models.OneToOneField(Profesori, on_delete=models.SET_NULL, null=True, blank=True, related_name="tutore_student") #daca sterg prof, tutore sa devina null
    def __str__ (self):
        return self.email
    

class Create_Student_request(serializers.Serializer):
    nume=serializers.CharField()
    email=serializers.CharField()
    an_universitar=serializers.IntegerField()

class Student_serializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"
