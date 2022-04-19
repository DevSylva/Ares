from django.urls import path
from . import views

urlpatterns = [
    path('event/', views.eventView),
    path('eventDetail/<int:pk>/', views.eventDetailView),
]
