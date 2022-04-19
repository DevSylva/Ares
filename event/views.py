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
from .models import Event
from .serializers import EventSerialzer


@api_view(["GET", "POST"])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def eventView(request):
    events = Event.objects.all()

    # GET request
    if request.method == "GET":
        serializer = EventSerialzer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST request
    elif request.method == "POST":
        eventData = request.data
        serializer = EventSerialzer(data=eventData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def eventDetailView(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response("Event does not exist", status=status.HTTP_200_OK)

    # GET request
    if request.method == "GET":
        serializer = EventSerialzer(event)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT request
    elif request.method == "PUT":
        eventData = request.data
        serializer = EventSerialzer(event, data=eventData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_Ok)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE request
    elif request.method == "DELETE":
        event.delete()
        return Response(status=status.HTTP_200_OK)