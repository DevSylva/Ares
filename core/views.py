from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from account.models import User
from .models import *
from .forms import PaymentForm, TopUpForm, WithdrawalForm
from django.contrib import messages
from .utils import Util
import time



def home(request):
    if request.user.is_authenticated:
        return redirect("core:dashboard")
    else:
        return redirect("account:sign-in")
    # return render(request, 'index.html')

@login_required(login_url='account:sign-in')
def dashboard(request):
    logged_in_user = request.user
    Users = User.objects.all().count() + 36999
    user = User.objects.get(email=request.user)

    data = {
        "logged_in_user": logged_in_user,
        "Users": Users,
        "page": "dashboard",
        "user": user,
    }
    
    return render(request, "dashboard.html", context=data)

@login_required(login_url="account:sign-in")
def profile(request):
    user = User.objects.get(email=request.user)

    data = {
        'full_name': f"{user.first_name} {user.last_name}",
        'page': "profile",
        'user': user,
    }
    return render(request, "profile.html", context=data)

@login_required(login_url="account:sign-in")
def transactions(request):
    transaction_s = Transaction.objects.filter(user=request.user.id)

    data = {
        "transactions": transaction_s,
        "page": "teachers",
        "page": "transactions",
    }
    return render(request, "transactions.html", context=data)

@login_required(login_url="account:sign-in")
def deposit(request):
    wallet = Wallet.objects.all()
    if request.method == "POST":
        form = PaymentForm(request.POST or None, request.FILES or None)
        data = request.POST
        file = request.FILES
        print(f"file : {file}")
        print(data)
        if form.is_valid():
            depositor = form.save(commit=False)
            depositor.user = request.user
            depositor.save()
            print('done')
            messages.success(request, "We'll let you know once we receive your deposit")

            Transaction.objects.create(
                user=request.user,
                plan=Plan.objects.get(id=request.POST['plan']),
                amount = request.POST['amount'],
                status = "Pending",
                type="Deposit",
            )

            try:
                data = {
                    "subject": "Incoming Payment",
                    "body": "Hello boss, a payment of ${} has been initialized by {},confirm and approve payment.".format(request.POST['amount'], request.user)
                }
                Util.send_email(data)
                print("email has been successfully sent!")
            except Exception as e:
                print(e)

            return redirect("core:transactions")
        else:
            messages.error(request, form.errors)
            print(form.errors)
    else:
        form = PaymentForm()
    data = {
        "eth": Wallet.objects.get(name="Ethereum(ETH) Wallet"),
        "btc": Wallet.objects.get(name="Bitcoin(BTC) Wallet"),
        "form": form,
        "page": "deposit",
    }
    return render(request, "deposit.html", context=data)


@login_required(login_url="account:sign-in")
def topup(request):
    wallet = Wallet.objects.all()
    if request.method == "POST":
        form = TopUpForm(request.POST or None, request.FILES or None)
        data = request.POST
        file = request.FILES
        if form.is_valid():
            depositor = form.save(commit=False)
            depositor.user = request.user
            depositor.save()
            print('done')
            messages.success(
                request, "We'll let you know once we receive your deposit")

            Transaction.objects.create(
                user=request.user,
                plan=Plan.objects.get(id=request.POST['plan']),
                amount=request.POST['amount'],
                status="Pending",
                type="Deposit",
            )

            try:
                data = {
                    "subject": "Incoming Top-up",
                    "body": "Hello boss, a Top-up of ${} has been initialized by {},confirm and approve payment.".format(request.POST['amount'], request.user)
                }
                Util.send_email(data)
                print("email has been successfully sent!")
            except Exception as e:
                print(e)

            return redirect("core:transactions")
        else:
            messages.error(request, form.errors)
            print(form.errors)
    else:
        form = TopUpForm()
    data = {
        "eth": Wallet.objects.get(name="Ethereum(ETH) Wallet"),
        "btc": Wallet.objects.get(name="Bitcoin(BTC) Wallet"),
        "form": form,
        "page": "topup",
    }
    return render(request, "topup.html", context=data)

@login_required(login_url="account:sign-in")
def plan(request, id):
    investment_plan = Plan.objects.get(id=id)
    user = User.objects.get(email=request.user)
    data = {
        "plan": investment_plan,
        "user": user,
        "page": "plan",
    }
    return render(request, "plan.html", context=data)

@login_required(login_url="account:sign-in")
def bitcoin(request):
    return render(request, 'bitcoinqrcode.html')

@login_required(login_url="account:sign-in")
def ethereum(request):
    return render(request, 'ethereumqrcode.html')

@login_required(login_url="account:sign-in")
def withdraw(request):
    
    data = {
        "page": "withdraw"
    }

    return render(request, "withdraw.html", context=data)


@login_required(login_url="account:sign-in")
def payout(request):
    if request.method == "POST":
        form = WithdrawalForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            payee = form.save(commit=False)
            payee.user = request.user
            payee.save()
            print('done')
            
            try:
                data = {
                    "subject": "Withdrawal Initiated",
                    "body": "Hello, a withdrawal of ${} has been initialized by {},confirm and approve payment.".format(request.POST['amount'], request.user)
                }
                Util.send_email(data)
                print("email has been successfully sent!")
            except Exception as e:
                print(e)

            return redirect("core:withdraw")
        else:
            messages.error(request, form.errors)
            print(form.errors)
    else:
        form = WithdrawalForm()
    data = {
        "form": form,
        "page": "withdraw",
    }
    return render(request, "payout.html", context=data)
