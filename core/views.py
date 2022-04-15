from email.policy import HTTP
from django.shortcuts import render
import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from core.models import (
    Pupil,
    Teacher,
    Staff,
    Class
)
from .serializers import (
    PupilSerializer
)
# Create your views here.

@api_view(["GET", "POST"])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def pupilView(request):
    if request.method == "GET":
        pupils = Pupil.objects.all()
        serializer = PupilSerializer(pupils, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        pupilData = request.data
        print(pupilData)
        serializer = PupilSerializer(data=pupilData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
