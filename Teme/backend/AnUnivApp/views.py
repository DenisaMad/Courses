from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from .models import AnUniversitar, AnUniv_serializer, Create_AnUniv_request
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

'''# Create your views here.
@api_view(["POST"])
def an_universitar(request):
    an_start=input("Introduceti inceputul anului universitar: ")
    an_end=input("Introduceti sfarsitul anului universitar: ")
   
    AnUniversitar.objects.create(an_start=an_start, an_end=an_end)
    print("Profesor salvat cu succes")
    return Response("Succes")'''


class Create_AnUniv_view(APIView):
    @swagger_auto_schema(request_body=Create_AnUniv_request)
    def post(self, request):
        validate= AnUniv_serializer(data=request.data)
        if validate.is_valid():
            validate.save()
            return Response("An universitar creat cu succes", status.HTTP_201_CREATED)
        else : 
            errors=validate.errors
            return Response(errors, status.HTTP_400_BAD_REQUEST)