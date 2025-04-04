from django.shortcuts import render
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
from .forms import PaymentForm

def index(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Get the phone number and amount from the form
            phone_number = form.cleaned_data['phone_number']
            amount = form.cleaned_data['amount']
            
            # Convert amount to integer (in cents)
            amount_in_cents = int(amount * 1)  # Convert amount to cents
            
            cl = MpesaClient()
            account_reference = 'reference'
            transaction_desc = 'Description'
            callback_url = 'https://api.darajambili.com/express-payment'
            response = cl.stk_push(phone_number, amount_in_cents, account_reference, transaction_desc, callback_url)
            return HttpResponse(response)
    else:
        form = PaymentForm()

    return render(request, 'payments/index.html', {'form': form})
