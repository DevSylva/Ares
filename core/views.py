from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated:
        return redirect("core:dashboard")
    else:
        return redirect("account:sign-in")


@login_required(login_url='account:sign-in')
def dashboard(request):
    logged_in_user = request.user
    data = {
        "logged_in_user": logged_in_user
    }
    return render(request, "dashboard.html", context=data)


@login_required(login_url="account:sign-in")
def profile(request):
    return render(request, "profile.html")