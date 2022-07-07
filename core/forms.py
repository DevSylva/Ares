from django import forms
from core.models import *

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('amount', 'receipt', 'plan', 'duration')

class TopUpForm(forms.ModelForm):
    class Meta:
        model = TopUp
        fields = ('amount', 'receipt', 'plan')


class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = Withdraw
        fields = ('amount', 'plan', 'crypto_id', 'wallet_address')
