from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('profile/', views.profile, name="profile"),
    path('transactions/', views.transactions, name="transactions"),
    path('billing/', views.billing, name="billing"),
    path('deposit/', views.deposit, name="deposit"),
    path('plan/<int:id>/', views.plan, name="plan"),
    path('bitcoin-qr-code/', views.bitcoin, name="bitcoin"),
    path('ethereum-qr-code/', views.ethereum, name="ethereum"),
]