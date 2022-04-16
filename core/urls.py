from django.urls import path
from core import views

urlpatterns = [
    # pupil paths
    path('pupil/', views.pupilView),
    path('pupilDetail/<int:pk>/', views.pupilDetailView),

    # teacher paths
    path('teacher/', views.teacherView),
    path('teacherDetail/<int:pk>/', views.teacherDetailView),

    # staff paths
    path('staff/', views.staffView),
    path('staffDetail/<int:pk>/', views.staffDetailView),
]
