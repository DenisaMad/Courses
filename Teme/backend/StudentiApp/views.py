from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
# Create your views here.

@api_view(["GET"])
def Test(request):
    print("Functia apelata")
    return Response("Succes")

@api_view(["GET"])
def Test2(request):
    print("Buna ziua")
    return Response("Save")

@api_view(["POST"])
def salveaza_user(request):
    name=input("Introduceti numele utilizatorului: ")
    email=input("Introduceti email-ul utilizatorului: ")
    an_universitar=input("Introduceti anul univerisatar:  ")
    Student.objects.create(nume=name, email=email, an_universitar_id=an_universitar)
    print("User salvat cu succes")
    return Response("Succes")
