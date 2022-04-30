from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from account.models import User
from .models import Teacher


def home(request):
    if request.user.is_authenticated:
        return redirect("core:dashboard")
    else:
        return redirect("account:sign-in")


@login_required(login_url='account:sign-in')
def dashboard(request):
    logged_in_user = request.user
    Users = User.objects.all().count()
    Teachers = Teacher.objects.all().count()

    data = {
        "logged_in_user": logged_in_user,
        "Users": Users,
        "Teachers": Teachers,
    }
    return render(request, "dashboard.html", context=data)


@login_required(login_url="account:sign-in")
def profile(request):
    user = User.objects.get(email=request.user)

    if user.first_name and user.last_name:
        current_user = "{} {}".format(user.first_name.title(), user.last_name.title())
    else:
        current_user = user.username

    data = {
        'user': current_user,
    }
    return render(request, "profile.html", context=data)


@login_required(login_url="account:sign-in")
def teachers(request):
    teachers = Teacher.objects.all()

    data = {
        "teachers": teachers
    }
    return render(request, "teachers.html", context=data)
