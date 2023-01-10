from django.shortcuts import render
from tel_app.forms import ContactForm, PayForm
from tel_app.models import Contact, Pay

def reg_form(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        _ = Contact.objects.get_or_create(
            name=form.cleaned_data['name'],
            password=form.cleaned_data['password'],
            email=form.cleaned_data['email']
        )
    return render(request, 'index.html', {'form': form})


def credit_card(request):
    text = ["Card number", "Name", "Date", "CVV/CVN"]
    card = PayForm(request.POST)
    if card.is_valid():
        _ = Pay.objects.get_or_create(
            number=card.cleaned_data['number'],
            name=card.cleaned_data['name'],
            date=card.cleaned_data['date'],
            cvv=card.cleaned_data['cvv']
        )
    return render(request, 'pay.html', {'card': card, 'text': text})