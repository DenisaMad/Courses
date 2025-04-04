from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from .models import Profesori, Create_Profesor_request, Profesor_serializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status



# Create your views here.
#@api_view(["POST"])
#def salveaza_profesor(request):
 #   name=input("Introduceti numele profesorului: ")
  #  email=input("Introduceti email-ul profesorului: ")
   # departament=input("Introduceti departamentul:  ")
    #Profesori.objects.create(nume=name, email=email, departament=departament)
    #print("Profesor salvat cu succes")
    #return Response("Succes")
#class Create_teacher_view(APIView):
    #@swagger_auto_schema(request_body=Create_Profesor_request)
    #def post(self, request):
       # Profesori.objects.create(nume=name, email=email, departament=departament)
     #   print(request.data)
      #  n=request.data.get("name")
     #   e=request.data.get("email")
      #  d=request.data.get("departament")
       # if len(n)>30 : 
         #   return Response ("Numele nu trebuie sa depaseasca 30 de caractere!!!!",status.HTTP_400_BAD_REQUEST)
        #if len(e)>30 : 
          #  return Response ("Email-ul nu trebuie sa depaseasca 50 de caractere!!!!",status.HTTP_400_BAD_REQUEST)
        #Profesori.objects.create(nume=n, email=e, departament=d)
        #return Response("Succes")

class Create_teacher_view(APIView):
    @swagger_auto_schema(request_body=Create_Profesor_request)
    def post(self, request):
        validate= Profesor_serializer(data=request.data)
        if validate.is_valid():
            validate.save()
            return Response("Profesor creat cu succes", status.HTTP_201_CREATED)
        else : 
            errors=validate.errors
            return Response(errors, status.HTTP_400_BAD_REQUEST)