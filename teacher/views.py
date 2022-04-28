from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Teacher

# Create your views here.
@login_required(login_url="account:sign-in")
def teachers(request):
    teachers = Teacher.objects.all()

    data = {
        "teachers": teachers
    }
    return render(request, "teachers.html", context=data)
