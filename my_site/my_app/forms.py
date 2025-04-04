from django import forms

class PaymentForm(forms.Form):
    phone_number = forms.CharField(max_length=15, required=True, label='Phone Number')
    amount = forms.DecimalField(max_digits=10, decimal_places=2, required=True, label='Amount')
