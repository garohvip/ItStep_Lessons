import pymysql
from easygui import *


with open("pass.txt", "r") as file:
    pw = file.readlines()
pw = [line.rstrip() for line in pw]
try:
    connection = pymysql.connect(
        host=pw[0],
        port=int(pw[1]),
        user=pw[2],
        password=pw[3],
        database=pw[4],
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        while True:
            enter = buttonbox("Choose:", "Choose", ["Вывод", "Добавить", "Удалить", "Изменить"])
            if enter == "Вывод":
                output = buttonbox("Выберите, по какому критерию делать вывод пользователей:\n\n1 - Вывод всех\n2 - За возрастом\n3 - По городу\n4 - По стране\n5 - По id", "Choose", ["1", "2", "3", "4", "5"])
                if output == "1":
                    with connection.cursor() as cursor:
                        cursor.execute("""SELECT * FROM `peoples` WHERE rem = '-';""")
                        result = cursor.fetchall()
                        output_all_info_string = []
                        for i in result:
                            output_all_info_string.append(f"id: {i['id']}\nName: {i['name']}\nSurname: {i['surname']}\nCity: {i['city']}\nCountry: {i['country']}\nBirthday: {i['birthday']}\n")
                        if buttonbox("\n".join(output_all_info_string), "Save", ["Save", "Cancel"]) == "Save":
                            save_output = filesavebox(msg='Save .txt File', title="Save", default="output_information")
                            with open(save_output + ".txt", "w") as file:
                                file.write("\n".join(output_all_info_string))

                elif output == "2":
                    output_addit = buttonbox("Какой вывод нужен?", "Choose", ["За диапазоном возрастов", "За одним возрастом"])
                    if output_addit == "За диапазоном возрастов":
                        with connection.cursor() as cursor:
                            enter_age = multenterbox("Введите диапазон возраста:", "Enter", ["От:", "До:"])
                            cursor.execute(f"""SELECT * FROM `peoples` WHERE YEAR(birthday) >= YEAR(NOW()) - {int(enter_age[1])} AND YEAR(birthday) <= YEAR(NOW()) - {int(enter_age[0])} AND rem = '-';""")
                            result = cursor.fetchall()
                            if result:
                                output_year_info_string = []
                                for i in result:
                                    output_year_info_string.append(f"id: {i['id']}\nName: {i['name']}\nSurname: {i['surname']}\nCity: {i['city']}\nCountry: {i['country']}\nBirthday: {i['birthday']}\n")
                                if buttonbox("\n".join(output_year_info_string), "Save", ["Save", "Cancel"]) == "Save":
                                    save_output = filesavebox(msg='Save .txt File', title="Save", default="output_information")
                                    with open(save_output + ".txt", "w") as file:
                                        file.write("\n".join(output_year_info_string))
                            else:
                                msgbox("Пользователей не найдено!")

                    elif output_addit == "За одним возрастом":
                        with connection.cursor() as cursor:
                            enter_age = enterbox("Введите возраст:", "Enter")
                            cursor.execute(f"""SELECT * FROM `peoples` WHERE YEAR(birthday) = YEAR(NOW()) - {int(enter_age)} AND rem = '-';""")
                            result = cursor.fetchall()
                            if result:
                                output_year_info_string = []
                                for i in result:
                                    output_year_info_string.append(f"id: {i['id']}\nName: {i['name']}\nSurname: {i['surname']}\nCity: {i['city']}\nCountry: {i['country']}\nBirthday: {i['birthday']}\n")
                                if buttonbox("\n".join(output_year_info_string), "Save", ["Save", "Cancel"]) == "Save":
                                    save_output = filesavebox(msg='Save .txt File', title="Save", default="output_information")
                                    with open(save_output + ".txt", "w") as file:
                                        file.write("\n".join(output_year_info_string))
                            else:
                                msgbox("Пользователей не найдено!")

                elif output == "3":
                    with connection.cursor() as cursor:
                        enter_city = enterbox("Введите город:", "Enter")
                        cursor.execute(f"""SELECT * FROM `peoples` WHERE city = '{enter_city}' AND rem = '-';""")
                        result = cursor.fetchall()
                        if result:
                            output_year_info_string = []
                            for i in result:
                                output_year_info_string.append(f"id: {i['id']}\nName: {i['name']}\nSurname: {i['surname']}\nCity: {i['city']}\nCountry: {i['country']}\nBirthday: {i['birthday']}\n")
                                if buttonbox("\n".join(output_year_info_string), "Save", ["Save", "Cancel"]) == "Save":
                                    save_output = filesavebox(msg='Save .txt File', title="Save", default="output_information")
                                    with open(save_output + ".txt", "w") as file:
                                        file.write("\n".join(output_year_info_string))
                        else:
                            msgbox("Пользователей не найдено!")

                elif output == "4":
                    with connection.cursor() as cursor:
                        enter_country = enterbox("Введите страну:", "Enter")
                        cursor.execute(f"""SELECT * FROM `peoples` WHERE country = '{enter_country}' AND rem = '-';""")
                        result = cursor.fetchall()
                        if result:
                            output_year_info_string = []
                            for i in result:
                                output_year_info_string.append(f"id: {i['id']}\nName: {i['name']}\nSurname: {i['surname']}\nCity: {i['city']}\nCountry: {i['country']}\nBirthday: {i['birthday']}\n")
                                if buttonbox("\n".join(output_year_info_string), "Save", ["Save", "Cancel"]) == "Save":
                                    save_output = filesavebox(msg='Save .txt File', title="Save", default="output_information")
                                    with open(save_output + ".txt", "w") as file:
                                        file.write("\n".join(output_year_info_string))
                        else:
                            msgbox("Пользователей не найдено!")

                elif output == "5":
                    with connection.cursor() as cursor:
                        enter_id = enterbox("Введите id:", "Enter")
                        cursor.execute(f"""SELECT * FROM `peoples` WHERE id = {int(enter_id)} AND rem = '-';""")
                        result = cursor.fetchall()
                        if result:
                            output_all_info_string = []
                            output_all_info_string.append(f"id: {result[0]['id']}\nName: {result[0]['name']}\nSurname: {result[0]['surname']}\nCity: {result[0]['city']}\nCountry: {result[0]['country']}\nBirthday: {result[0]['birthday']}\n")
                            if buttonbox("\n".join(output_all_info_string), "Save", ["Save", "Cancel"]) == "Save":
                                save_output = filesavebox(msg='Save .txt File', title="Save", default="output_information")
                                with open(save_output + ".txt", "w") as file:
                                    file.write("\n".join(output_all_info_string))
                        else:
                            msgbox("Пользователей не найдено!")

            elif enter == "Добавить":
                enter_new_user = multenterbox("Введите данные нового пользователя:\n\n(Дату вводить в формате ГГГГ.ММ.ДД)\n\nОбязательное заполнение всех полей!", "Enter", ["Name:", "Surname:", "City:", "Country:", "Birthday:"])
                if enter_new_user[0] and enter_new_user[1] and enter_new_user[2] and enter_new_user[3] and enter_new_user[4]:
                    with connection.cursor() as cursor:
                        cursor.execute(f"""INSERT INTO `peoples` (name, surname, city, country, birthday) VALUES ('{enter_new_user[0]}', '{enter_new_user[1]}', '{enter_new_user[2]}', '{enter_new_user[3]}', '{enter_new_user[4]}');""")
                        connection.commit()
                        cursor.execute(f"""SELECT id FROM `peoples` WHERE name = '{enter_new_user[0]}' AND surname = '{enter_new_user[1]}' AND city = '{enter_new_user[2]}' AND country = '{enter_new_user[3]}' AND birthday = '{enter_new_user[4]}'""")
                        result = cursor.fetchall()
                        msgbox(f"Пользователь успешно добавлен!\n\nid нового пользователя: {result[0]['id']}")
                else:
                    msgbox("Обязательное заполнение всех полей!")

            elif enter == "Удалить":
                enter_del_user = enterbox("Введите id пользователя, которого хотите удалить:", "Enter")
                if enter_del_user:
                    with connection.cursor() as cursor:
                        cursor.execute(f"""SELECT * FROM `peoples` WHERE id = {enter_del_user} AND rem = '-';""")
                        result = cursor.fetchall()
                        if result:
                            with connection.cursor() as cursor:
                                cursor.execute(f"""UPDATE `peoples` SET rem = "+" WHERE id = {enter_del_user};""")
                                connection.commit()
                                msgbox(f"Пользователь успешно удален из БД!")
                        else:
                            msgbox("Пользователя не найдено!")
                else:
                    msgbox("Обязательное заполнение всех полей!")

            elif enter == "Изменить":
                enter_update_user = enterbox("Введите id пользователя, которому хотите изменить данные:", "Enter")
                if enter_update_user:
                    with connection.cursor() as cursor:
                        cursor.execute(f"""SELECT * FROM `peoples` WHERE id = {enter_update_user} AND rem = '-';""")
                        result = cursor.fetchall()
                        if result:
                            slash_n = '\n'
                            what_update = multenterbox(f"""{f"id: {result[0]['id']}{slash_n}Na"
                                                            f"me: {result[0]['name']}{slash_n}Surna"
                                                            f"me: {result[0]['surname']}{slash_n}Cit"
                                                            f"y: {result[0]['city']}{slash_n}Coun"
                                                            f"try: {result[0]['country']}{slash_n}Birt"
                                                            f"hday: {result[0]['birthday']}"}\n\nВведите данные нового пользователя:\n\nЗаполнение всех полей обязательно!\n\n(Дату вводить в формате ГГГГ.ММ.ДД)""", "Enter", ["Name:", "Surname:", "City:", "Country:", "Birthday:"])
                            next_action = 0
                            for i in what_update:
                                if i == "":
                                    msgbox("Все поля должны быть заполнены!")
                                    break
                                else:
                                    next_action += 1
                            if next_action == 5:
                                with connection.cursor() as cursor:
                                    cursor.execute(f"""UPDATE `peoples` SET name = '{what_update[0]}', surname = '{what_update[1]}', city = '{what_update[2]}', country = '{what_update[3]}', birthday = '{what_update[4]}' WHERE id = {enter_update_user};""")
                                    connection.commit()
                                    msgbox(f"Данные пользователя успешно изменены!")
                        else:
                            msgbox("Пользователя не найдено!")
                else:
                    msgbox("Обязательное заполнение всех полей!")

            else:
                break
    finally:
        connection.close()
except Exception as ex:
    print(ex)