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
)
from .serializers import (
    PupilSerializer,
    TeacherSerializer,
    StaffSerializer,
)
# Create your views here.


@api_view(["GET", "POST"])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def pupilView(request):
    pupils = Pupil.objects.all()

    # GET request
    if request.method == "GET":
        serializer = PupilSerializer(pupils, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST request
    elif request.method == "POST":
        pupilData = request.data
        serializer = PupilSerializer(data=pupilData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def pupilDetailView(request, pk):
    try:
        pupil = Pupil.objects.get(pk=pk)
    except Pupil.DoesNotExist:
        return Response("Pupil does not exist", status=status.HTTP_200_OK)

    # GET request
    if request.method == "GET":
        serializer = PupilSerializer(pupil)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT request
    elif request.method == "PUT":
        pupilData = request.data
        serializer = PupilSerializer(pupil, data=pupilData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_Ok)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE request
    elif request.method == "DELETE":
        pupil.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def teacherView(request):
    teachers = Teacher.objects.all()

    if request.method == "GET":
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        teacherData = request.data
        serializer = TeacherSerializer(data=teacherData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def teacherDetailView(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return Response("Teacher Does not Exist", status=status.HTTP_200_OK)

    if request.method == "GET":
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        teacherData = request.data
        serializer = TeacherSerializer(teacher, data=teacherData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_Ok)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        teacher.delete()
        return Response("Teacher has been delete", status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def staffView(request):
    staffs = Staff.objects.all()

    if request.method == "GET":
        serializer = StaffSerializer(staffs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        staffData = request.data
        serializer = StaffSerializer(data=staffData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def staffDetailView(request, pk):
    try:
        staff = Staff.objects.get(pk=pk)
    except Staff.DoesNotExist:
        return Response("Staff Does not Exist", status=status.HTTP_200_OK)

    if request.method == "GET":
        serializer = StaffSerializer(staff)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        staffData = request.data
        serializer = TeacherSerializer(staff, data=staffData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_Ok)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        staff.delete()
        return Response("Teacher has been delete", status=status.HTTP_200_OK)
