from django.core.mail import EmailMessage
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
