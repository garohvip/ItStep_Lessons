from django.shortcuts import render
from first_app.models import *
import datetime


def books(request):
    content = Book.objects.all()
    all_categories = Categirie.objects.all()
    return render(template_name='index.html', request=request, context={'content': content, 'all_categories': all_categories})


def books_year(request, flag):
    all_categories = Categirie.objects.all()
    if flag == "before_1880":
        content = Book.objects.filter(yearCreate__lte=datetime.date(1880, 1, 1))
        return render(template_name='index.html', request=request, context={'content': content, 'all_categories': all_categories})
    elif flag == "after_1880":
        content = Book.objects.filter(yearCreate__gte=datetime.date(1880, 1, 1))
        return render(template_name='index.html', request=request, context={'content': content, 'all_categories': all_categories})
    elif flag == flag:
        content = Book.objects.filter(style__name=flag)
        return render(template_name='index.html', request=request, context={'content': content, 'all_categories': all_categories})
