from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import AnUniversitar

# Create your views here.
@api_view(["POST"])
def an_universitar(request):
    an_start=input("Introduceti inceputul anului universitar: ")
    an_end=input("Introduceti sfarsitul anului universitar: ")
   
    AnUniversitar.objects.create(an_start=an_start, an_end=an_end)
    print("Profesor salvat cu succes")
    return Response("Succes")