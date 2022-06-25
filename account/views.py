import mailbox
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
from core.views import dashboard
from .forms import SignUpForm
from .utils import Util
# Create your views here.


def sign_in(request):
    if request.user.is_authenticated and request.method == "GET":
        return redirect("core:dashboard")

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
                return redirect("core:dashboard")
                
            else:
                messages.error(request, "User does not exit")
        else:
            messages.error(request, form.errors)
            return redirect("account:sign-in")

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

            # notify me of this signup
            try:
                data = {
                    "subject": "New User SignUp",
                    "body": "Hey!, you have a recently signup from {}".format(request.POST['email'])
                }
                Util.send_email(data)
                print("email has been successfully sent!")
            except Exception as e:
                print(e)

            login(request, user)

            # send the user a mailbox
            try:
                useremail = request.user.email
                html_content = render_to_string(
                    "welcome.html")
                text_content = strip_tags(html_content)

                email = EmailMultiAlternatives(
                    subject="Welcome to Ares",
                    body=text_content,
                    from_email="aresherokuapps@gmail.com",
                    to=[request.POST['email'], ]
                )
                email.attach_alternative(html_content, "text/html")
                email.send()
            except Exception as e:
                print(e)

            return redirect("core:home")
        else:
            messages.error(request, form.errors)
            print(form.errors)
    form = SignUpForm()
    return render(request, "sign-up.html", context={"form": form})


def sign_out(request):
    logout(request)
    return redirect("account:sign-in")
