from django.urls import path
from . import views

app_name = "teacher"

urlpatterns = [
    path('', views.teachers, name="teachers"),
]
