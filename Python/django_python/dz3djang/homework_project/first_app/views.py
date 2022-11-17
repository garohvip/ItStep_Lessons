from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import pymysql


def check_views(request, table_sql):
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user="root",
        password="DataBase0321",
        database="prshop",
        cursorclass=pymysql.cursors.DictCursor
    )
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT nameProduct FROM `{table_sql}`""")
        all_data = cursor.fetchall()
    if all_data:
        data = "<br>".join([f"{i.get('nameProduct')}" for i in all_data])
        return HttpResponse(f"Продукты в БД:<br><br>{data.title()}")
    else:
        return HttpResponse(f"Продуктов нет в БД!")


def add_views(request, table_sql, nameProduct):
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user="root",
        password="DataBase0321",
        database="prshop",
        cursorclass=pymysql.cursors.DictCursor
    )
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT nameProduct FROM `{table_sql}` WHERE nameProduct = '{nameProduct}'""")
        data = cursor.fetchone()
    if data:
        return HttpResponse(f"Продукт '{nameProduct}' уже есть в БД!")
    else:
        with connection.cursor() as cursor:
            cursor.execute(f"""INSERT INTO `{table_sql}` (nameProduct) VALUES ('{nameProduct}')""")
            connection.commit()
        return HttpResponse(f"Продукт '{nameProduct}' успешно добавлен в БД!")


def del_views(request, table_sql, nameProduct):
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user="root",
        password="DataBase0321",
        database="prshop",
        cursorclass=pymysql.cursors.DictCursor
    )
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT nameProduct FROM `{table_sql}` WHERE nameProduct = '{nameProduct}'""")
        data = cursor.fetchone()
    if data:
        with connection.cursor() as cursor:
            cursor.execute(f"""DELETE FROM `{table_sql}` WHERE nameProduct = '{nameProduct}'""")
            connection.commit()
        return HttpResponse(f"Продукт '{nameProduct}' успешно удален из БД!")
    else:
        return HttpResponse(f"Продукта '{nameProduct}' нет в БД!")


def year_old(request, year):
    if 1920 <= int(year) <= 1999:
        return HttpResponse(f"{year}")
    else:
        return HttpResponse(f"Не верная дата")


def number_phone(request, number):
    return HttpResponse(f"{number}")


def mail_post(request, mail):
    return  HttpResponse(f"{mail}")