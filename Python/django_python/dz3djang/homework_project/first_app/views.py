from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import pymysql


def home_page(request):
    # return HttpResponse(f"Главная страница")
    return render(request, 'index.html', context={'text': 'Главная страница', 'page_list': [('news', "Новости"), ('management', "Управленцы компанией"), ('faq', "Про компанию"), ('contact', "Контакты")]})


def news(request, city):
    if city == "london":
        return HttpResponse(f"London is the capital of great Britain")
    elif city == "kyiv":
        return HttpResponse(f"Столица Украины!")
    else:
        return HttpResponse(f"Страница новостей<br><div><a href='http://127.0.0.1:8000/'>Главная страница</a></div>")



def management(request, who):
    if who == "owner":
        return HttpResponse(f"Здесь будет имя основателя")
    elif who == "manager":
        return HttpResponse(f"Здесь будет имя менеджера")
    else:
        return HttpResponse(f"Управленцы компанией<br><div><a href='http://127.0.0.1:8000/'>Главная страница</a></div>")



def faq(request):
    return HttpResponse(f"Про компанию<br><div><a href='http://127.0.0.1:8000/'>Главная страница</a></div>")


def contact(request):
    return HttpResponse(f"Здесь будут контакты<br><div><a href='http://127.0.0.1:8000/'>Главная страница</a></div>")


# def check_views(request, table_sql):
#     connection = pymysql.connect(
#         host='localhost',
#         port=3306,
#         user="root",
#         password="DataBase0321",
#         database="prshop",
#         cursorclass=pymysql.cursors.DictCursor
#     )
#     with connection.cursor() as cursor:
#         cursor.execute(f"""SELECT nameProduct FROM `{table_sql}`""")
#         all_data = cursor.fetchall()
#     if all_data:
#         data = "<br>".join([f"{i.get('nameProduct')}" for i in all_data])
#         return HttpResponse(f"Продукты в БД:<br><br>{data.title()}")
#     else:
#         return HttpResponse(f"Продуктов нет в БД!")
#
#
# def add_views(request, table_sql, nameProduct):
#     connection = pymysql.connect(
#         host='localhost',
#         port=3306,
#         user="root",
#         password="DataBase0321",
#         database="prshop",
#         cursorclass=pymysql.cursors.DictCursor
#     )
#     with connection.cursor() as cursor:
#         cursor.execute(f"""SELECT nameProduct FROM `{table_sql}` WHERE nameProduct = '{nameProduct}'""")
#         data = cursor.fetchone()
#     if data:
#         return HttpResponse(f"Продукт '{nameProduct}' уже есть в БД!")
#     else:
#         with connection.cursor() as cursor:
#             cursor.execute(f"""INSERT INTO `{table_sql}` (nameProduct) VALUES ('{nameProduct}')""")
#             connection.commit()
#         return HttpResponse(f"Продукт '{nameProduct}' успешно добавлен в БД!")
#
#
# def del_views(request, table_sql, nameProduct):
#     connection = pymysql.connect(
#         host='localhost',
#         port=3306,
#         user="root",
#         password="DataBase0321",
#         database="prshop",
#         cursorclass=pymysql.cursors.DictCursor
#     )
#     with connection.cursor() as cursor:
#         cursor.execute(f"""SELECT nameProduct FROM `{table_sql}` WHERE nameProduct = '{nameProduct}'""")
#         data = cursor.fetchone()
#     if data:
#         with connection.cursor() as cursor:
#             cursor.execute(f"""DELETE FROM `{table_sql}` WHERE nameProduct = '{nameProduct}'""")
#             connection.commit()
#         return HttpResponse(f"Продукт '{nameProduct}' успешно удален из БД!")
#     else:
#         return HttpResponse(f"Продукта '{nameProduct}' нет в БД!")


# def year_old(request, year):
#     if 1920 <= int(year) <= 1999:
#         return HttpResponse(f"{year}")
#     else:
#         return HttpResponse(f"Не верная дата")
#
#
# def number_phone(request, number):
#     return HttpResponse(f"{number}")
#
#
# def mail_post(request, mail):
#     return  HttpResponse(f"{mail}")