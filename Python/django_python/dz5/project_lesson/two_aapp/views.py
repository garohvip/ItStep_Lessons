import base64
import os.path
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
import pymysql
import datetime


def dictsort(request):
    context = {"questions": [
        {'id': 2,
         'author': 'oliver',
         'question_text': 'Что первично, дух или материя?',
         'date': datetime.date(year=2006, month=7, day=14)
         },
        {'id': 3,
         'author': 'anthony',
         'question_text': 'Существует ли свобода воли?',
         'date': datetime.date(year=2007, month=7, day=14)},
        {'id': 1,
         'author': 'annie',
         'question_text': 'В чем смысл жизни?',
         'date': datetime.date(year=2005, month=7, day=14)}
    ]}
    return render(template_name='index1.html', request=request, context=context)


def images(request):
    try:
        connection = pymysql.connect(
            host="localhost",
            port=3306,
            user='root',
            password='DataBase0321',
            database='django_one',
            cursorclass=pymysql.cursors.DictCursor
        )
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT * FROM `table`""")
            image_64 = cursor.fetchall()
    except Exception as ex:
        print(ex)
    return render(template_name='index1.html', request=request, context={'img': image_64})


# def products(request):
#     content =
#     return render(template_name="index2.html", request=request, context={"products_list": content})