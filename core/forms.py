from django import forms
from core.models import *

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('amount', 'receipt', 'plan', 'duration')