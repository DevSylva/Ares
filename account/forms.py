from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import User
from django.core.exceptions import ValidationError


# Create your forms here.

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ("first_name", "last_name", "gender", "mobile",
                  "username", "email", "password1", "password2", "referral")

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
