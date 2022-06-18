from django.urls import path
from . import views
from account.api.views import *


app_name = "account"

urlpatterns = [
    path('sign-in/', views.sign_in, name="sign-in"),
    path('sign-up/', views.sign_up, name="sign-up"),
    path('sign-out/', views.sign_out, name="sign-out"),

    

    # api url path endpoint
    path('api/sign-up/', CustomUserCreate.as_view(), name='api-sign-up'),
    path('api/sign-in/', LoginView.as_view(), name='api-sign-in'),
]
