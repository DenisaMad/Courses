from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Profesori

# Create your views here.
@api_view(["POST"])
def salveaza_profesor(request):
    name=input("Introduceti numele profesorului: ")
    email=input("Introduceti email-ul profesorului: ")
    departament=input("Introduceti departamentul:  ")
    Profesori.objects.create(nume=name, email=email, departament=departament)
    print("Profesor salvat cu succes")
    return Response("Succes")