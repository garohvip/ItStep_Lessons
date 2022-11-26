from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# import pymysql


def home_page(request):
    # return HttpResponse(f"Главная страница")
    return render(request, 'index.html', context={'text': 'Главная страница', 'page_list': [('news', "Новости города"), ('gosduma', "Управленцы городом"), ('facts', "Факты про город"), ('contacts', "Телефонная книга местных служб"), ('history', "История города")]})


def news(request, where):
    if where == "factory":
        return HttpResponse(f"<h1>Здесь будут новости про завод</h1>")
    elif where == "metal":
        return HttpResponse(f"<h1>Здесь будут новости Металлургического района</h1>")
    else:
        return HttpResponse(f"Страница новостей города Кривой Рог<br><div><a href='http://127.0.0.1:8000/'>Главная страница</a></div>")


def gosduma(request, who):
    if who == "mer":
        return HttpResponse(f"Мэр Кривого Рога - Вилкул Александр Юрьевич")
    elif who == "gorglava":
        return HttpResponse(f"<h2>Вилкул Юрий Григорьевич - украинский общественный, политический и государственный деятель, профессор, доктор технических наук. Городской глава Кривого Рога</h2>")
    else:
        return HttpResponse(f"Управленцы городом<br><div><a href='http://127.0.0.1:8000/'>Главная страница</a></div>")


def facts(request, info):
    if info == "95kv":
        return HttpResponse(f"<h1>Здесь будет информация про 95 квартал</h1>")
    elif info == "artem":
        return HttpResponse(f"<h1>Здесь будет информация про район 'Артема'.</h1>")
    else:
        return HttpResponse(f"Факты города<br><div><a href='http://127.0.0.1:8000/'>Главная страница</a></div>")


def contacts(request, who):
    if who == "mer":
        return HttpResponse(f"<h2>Здесь будет номер телефона мэра Кривого Рога</h2>")
    elif who == "gorglava":
        return HttpResponse(f"<h2>Здесь будет номер телефона главы Кривого Рога</h2>")
    else:
        return HttpResponse(f"Здесь будут контакты<br><div><a href='http://127.0.0.1:8000/'>Главная страница</a></div>")


def history(request, info):
    if info == "people":
        return render(request, 'history_people.html', context={'text': 'Популярные люди города',
                                                      'page_list': [('Федосенко,_Павел_Юрьевич', "Федосенко Павел Юрьевич"),
                                                                    ('Сторожук,_Анатолий_Васильевич', "Сторожук Анатолий Васильевич"),
                                                                    ('Вилкул,_Юрий_Григорьевич', "Вилкул Юрий Григорьевич"),
                                                                    ('Бабич,_Юрий_Петрович', "Бабич Юрий Петрович")]})
    elif info == "photos":
        return render(request, 'history_photos.html', context={'text': 'Популярные люди города',
                                                      'page_list': [('%D0%9F%D0%B0%D1%80%D0%BA_%D0%93%D0%B5%D1%80%D0%BE%D0%B5%D0%B2', "File:%D0%9A%D1%80%D0%B8%D0%B2%D0%BE%D0%B9-%D0%A0%D0%BE%D0%B3-%D1%83%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0-%D1%87%D0%B0%D1%81%D1%8B-%D1%86%D0%B2%D0%B5%D1%82%D0%BE%D1%87%D0%BD%D1%8B%D0%B5-%D1%87%D0%B0%D1%81%D1%8B-95804.jpeg", "Цветочные часы"),
                                                                    ('Парк_имени_Фёдора_Мершавцева', "File:%D0%9F%D0%B0%D1%80%D0%BA_%D1%96%D0%BC%D0%B5%D0%BD%D1%96_%D0%A4%D0%B5%D0%B4%D0%BE%D1%80%D0%B0_%D0%9C%D0%B5%D1%80%D1%88%D0%B0%D0%B2%D1%86%D0%B5%D0%B2%D0%B0_-_%D0%BC%D1%96%D1%81%D1%82%D0%BE%D0%BA_%D1%87%D0%B5%D1%80%D0%B5%D0%B7_%D0%A1%D0%B0%D0%BA%D1%81%D0%B0%D0%B3%D0%B0%D0%BD%D1%8C.jpg", "Парк \"Правды\""),
                                                                    # ('Вилкул,_Юрий_Григорьевич', "Вилкул Юрий Григорьевич"),
                                                                    # ('Бабич,_Юрий_Петрович', "Бабич Юрий Петрович")
                                                                    ]})
    else:
        return HttpResponse(f"""Население в 1979 году составляло 650 000 человек. По переписи населения 1989 года составляло 723 000 человек, по переписи 2001 года составило 669 000 человек.

По состоянию на 1 декабря 2015 года в городе проживало 641 274 постоянных жителей и 642 788 человек наличного населения. Население на 1 декабря 2016 года — 638 395 постоянных жителей и 639 876 человек наличного населения. Население на 1 ноября 2017 года — 631 647 постоянных жителей и 633 128 человек наличного населения. По состоянию 1 января 2021 года в Кривом Роге насчитывалось 615,5 тысяч жителей.<br><div><h2><a href='http://127.0.0.1:8000/'>Главная страница</a></h2></div>""")

# def home_page(request):
#     # return HttpResponse(f"Главная страница")
#     return render(request, 'index.html', context={'text': 'Главная страница', 'page_list': [('news', "Новости"), ('management', "Управленцы компанией"), ('faq', "Про компанию"), ('contact', "Контакты")]})
#
#
# def news(request, city):
#     if city == "london":
#         return HttpResponse(f"London is the capital of great Britain")
#     elif city == "kyiv":
#         return HttpResponse(f"Столица Украины!")
#     else:
#         return HttpResponse(f"Страница новостей<br><div><a href='http://127.0.0.1:8000/'>Главная страница</a></div>")
#
#
#
# def management(request, who):
#     if who == "owner":
#         return HttpResponse(f"Здесь будет имя основателя")
#     elif who == "manager":
#         return HttpResponse(f"Здесь будет имя менеджера")
#     else:
#         return HttpResponse(f"Управленцы компанией<br><div><a href='http://127.0.0.1:8000/'>Главная страница</a></div>")
#
#
#
# def faq(request, info):
#     if info == "owner":
#         return HttpResponse(f"<h1>Здесь будет информация про основателя</h1>")
#     elif info == "manager":
#         return HttpResponse(f"<h1>Здесь будет информация про менеджера</h1>")
#     else:
#         return HttpResponse(f"Про компанию<br><div><a href='http://127.0.0.1:8000/'>Главная страница</a></div>")
#
#
# def contact(request, who):
#     if who == "owner":
#         return HttpResponse(f"<h2>Здесь будут контакты про основателя</h2>")
#     elif who == "manager":
#         return HttpResponse(f"<h2>Здесь будут контакты про менеджера</h2>")
#     else:
#         return HttpResponse(f"Здесь будут контакты<br><div><a href='http://127.0.0.1:8000/'>Главная страница</a></div>")


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
