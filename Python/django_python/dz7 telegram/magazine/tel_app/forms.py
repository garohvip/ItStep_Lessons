from django.forms import *


class ContactForm(forms.Form):
    name = CharField(label='name', required=False)
    password = CharField(label='password', required=False)
    email = EmailField(label='email', required=False)


class PayForm(forms.Form):
    number = IntegerField(label='Card number', required=False)
    name = CharField(label='Name', required=False)
    date = IntegerField(label='Date', required=False)
    cvv = IntegerField(label='CVV', required=False)