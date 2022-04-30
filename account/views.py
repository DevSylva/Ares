from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse

from core.views import dashboard
from .forms import SignUpForm
# Create your views here.


def sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        data = request.POST
        print(data)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("core:dashboard")
            else:
                messages.error(request, "Invalid username or password.")
                return redirect('account:sign-in')
        else:
            messages.error(request, "Invalid username or password.")
            
    form = AuthenticationForm()
    return render(request, "sign-in.html", context={"form": form})


def sign_up(request):
    if request.user.is_authenticated and request.method == "GET":
        return redirect("core:dashboard")

    if request.method == "POST":
        print(request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("core:home")
        else:
            messages.error(request, form.errors)
            print(form.errors)
    form = SignUpForm()
    return render(request, "sign-up.html", context={"form": form})


def sign_out(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("core:home")
