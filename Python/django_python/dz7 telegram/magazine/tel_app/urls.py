from django.contrib import admin
from django.urls import path, include
from tel_app.views import reg_form, credit_card

urlpatterns = [
    path('reg_form/', reg_form),
    path('pay_form/', credit_card)
]