from email.policy import HTTP
from django.shortcuts import render
import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from core.models import (
    Pupil
)
# Create your views here.

@api_view(["GET", "POST"])
def pupil(request):
    if request.method == "GET":
        return Response("GET Pupil", status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        return Response("POST Pupil", status=status.HTTP_200_OK)
