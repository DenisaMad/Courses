from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from .models import Student, Student_serializer, Create_Student_request
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

# Create your views here.
'''
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
    '''

class Create_Student_view(APIView):
    @swagger_auto_schema(request_body=Create_Student_request)
    def post(self, request):
        validate= Student_serializer(data=request.data)
        if validate.is_valid():
            validate.save()
            return Response("Student creat cu succes", status.HTTP_201_CREATED)
        else : 
            errors=validate.errors
            return Response(errors, status.HTTP_400_BAD_REQUEST)