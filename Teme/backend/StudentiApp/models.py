from django.db import models
from ProfesoriApp.models import Profesori
from AnUnivApp.models import AnUniversitar
# Create your models here.

class Student(models.Model):
    nume = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(unique=True, null=False, blank=False, max_length=50)
    an_universitar = models.ForeignKey(AnUniversitar,on_delete=models.SET_NULL, null=False, blank=False) 
    #am pus on delete=cascade ca imi dadea eroare, dar nu vad sensul de a sterge studentii daca se sterge profesorul
    profesori = models.ManyToManyField(Profesori, blank=True)
    tutore = models.OneToOneField(Profesori, on_delete=models.SET_NULL, null=True, blank=True, related_name="tutore_student") #daca sterg prof, tutore sa devina null