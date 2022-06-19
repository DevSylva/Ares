from django.utils.html import strip_tags
from django.template.loader import render_to_string, get_template
from django.core import mail
from django.core.mail import EmailMessage
from django.template import Context
from .views import *

class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data["subject"],
            body=data['body'],
            to=("sylvaejike@gmail.com",)
        )
        email.send()