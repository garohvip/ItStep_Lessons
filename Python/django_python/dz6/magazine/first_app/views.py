import base64
from django.shortcuts import render
from first_app.models import Book
import datetime


def books(request):
    content = Book.objects.all()
    return render(template_name='index.html', request=request, context={'content': content})
