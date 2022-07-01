from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('profile/', views.profile, name="profile"),
    path('transactions/', views.transactions, name="transactions"),
    path('deposit/', views.deposit, name="deposit"),
    path('top-up/', views.topup, name="topup"),
    path('withdraw/', views.withdraw, name="withdraw"),
    path('payout/', views.payout, name="payout"),
    path('plan/<int:id>/', views.plan, name="plan"),
    path('bitcoin-qr-code/', views.bitcoin, name="bitcoin"),
    path('ethereum-qr-code/', views.ethereum, name="ethereum"),
]