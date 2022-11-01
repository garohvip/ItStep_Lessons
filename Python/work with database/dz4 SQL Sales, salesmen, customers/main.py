import pymysql
from easygui import *

result = ""


def output_info(create_table):
    with connection.cursor() as cursor:
        cursor.execute(create_table)
        global result
        result = cursor.fetchall()
        output_for_easygui = []
        for i in result:
            output_for_easygui.append(f"perId: {i['perId']}\nidSalesmen: {i['idSalesmen']}\nnameSalesmen: {i['nameSalesmen']}\nphoneCustomers: {i['phoneCustomers']}\nnameProduct: {i['nameProduct']}\nsumma: {i['summa']}\n")
        if buttonbox("\n".join(output_for_easygui), "Output", ["Save", "Close"]) == "Save":
            save_output = filesavebox(msg='Save .txt File', title="Save", default="output_information")
            return save_output
        else:
            return "-"

def output_info_name(create_table):
    with connection.cursor() as cursor:
        cursor.execute(create_table)
        global result
        result = cursor.fetchall()
        for i in result[0]:
            if i == "idSalesmen":
                if buttonbox(f"idSalesmen: {result[0]['idSalesmen']}", "Output", ["Save", "Close"]) == "Save":
                    save_output = filesavebox(msg='Save .txt File', title="Save", default="output_information")
                    return save_output
                else:
                    return "-"
            elif i == "phoneCustomers":
                if buttonbox(f"phoneCustomers: {result[0]['phoneCustomers']}", "Output", ["Save", "Close"]) == "Save":
                    save_output = filesavebox(msg='Save .txt File', title="Save", default="output_information")
                    return save_output
                else:
                    return "-"
            elif i == "summa":
                if buttonbox(f"summa: {result[0]['summa']}", "Output", ["Save", "Close"]) == "Save":
                    save_output = filesavebox(msg='Save .txt File', title="Save", default="output_information")
                    return save_output
                else:
                    return "-"


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
    print("Welcome to the database")
    try:
        while True:
            enter = buttonbox("Choise:", "Choose", ["Изменить данные", "Добавить данные", "Вывести данные", "Удалить данные"])
            if enter == "Изменить данные":
                enter_update = buttonbox("Где хотите изменить?", "Choose", ["Таблица работников", "Таблица покупателей", "Таблица продаж"])
                if enter_update == "Таблица работников":
                    enter_update_salesmen = multenterbox("Введите ID сотрудника, которому хотите изменить "
                                                         "данные:\n\n(Оставьте поле пустым если не хотите его "
                                                         "менять)", "Enter", ["ID:", "Имя:", "Телефон:"])
                    with connection.cursor() as cursor:
                        create_table = f"SELECT * FROM `Salesmen` WHERE id = {enter_update_salesmen[0]};"
                        if cursor.execute(create_table):
                            if enter_update_salesmen[1] == "" and enter_update_salesmen[2] == "":
                                msgbox("Введите данные для добавления в БД")
                            elif enter_update_salesmen[1] == "":
                                new_info = f"UPDATE `Salesmen` SET phone = '{enter_update_salesmen[2]}' WHERE id = {enter_update_salesmen[0]};"
                            elif enter_update_salesmen[2] == "":
                                new_info = f"UPDATE `Salesmen` SET name = '{enter_update_salesmen[1]}' WHERE id = {enter_update_salesmen[0]};"
                            else:
                                new_info = f"UPDATE `Salesmen` SET name = '{enter_update_salesmen[1]}', phone = '{enter_update_salesmen[2]}' WHERE id = {enter_update_salesmen[0]};"
                        if new_info:
                            cursor.execute(new_info)
                            connection.commit()
                            msgbox("Данные успешно обновлены!")
                        else:
                            msgbox("Нет такого ID в БД!")

                elif enter_update == "Таблица покупателей":
                    enter_update_customers = multenterbox("Введите номер телефона покупателя, которому хотите изменить "
                                                         "данные:\n\n(Оставьте поле пустым если не хотите его "
                                                         "менять)", "Enter", ["Телефон:", "Имя:"])
                    with connection.cursor() as cursor:
                        create_table = f"SELECT * FROM `Customers` WHERE phone = {enter_update_customers[0]};"
                        if cursor.execute(create_table):
                            if enter_update_customers[1] == "":
                                msgbox("Введите данные для добавления в БД")
                            else:
                                new_info = f"UPDATE `Customers` SET name = '{enter_update_customers[1]}' WHERE phone = {enter_update_customers[0]};"
                                if new_info:
                                    cursor.execute(new_info)
                                    connection.commit()
                                    msgbox("Данные успешно обновлены!")
                        else:
                            msgbox("Нет такого покупателя в БД!")

            elif enter == "Добавить данные":
                enter_add = buttonbox("Что хотите добавить?:", "Choose", ["Нового продавца", "Нового покупателя", "Новую сделку"])
                if enter_add == "Нового продавца":
                    database1 = multenterbox("Введите данные нового продавца:", "Enter", ["Введите имя:", "Введите номер телефона:"])
                    if database1[0] and database1[1]:
                        with connection.cursor() as cursor:
                            insert = f"INSERT INTO `Salesmen` (name, phone) VALUES ('{database1[0]}', '{database1[1]}');"
                            cursor.execute(insert)
                            connection.commit()
                        with connection.cursor() as cursor:
                            insert = f"SELECT id FROM `Salesmen` WHERE name = '{database1[0]}' AND phone = '{database1[1]}';"
                            cursor.execute(insert)
                            result = cursor.fetchall()
                        msgbox(f"Информация успешно добавлена!\n\nID нового продавца: {result[0]['id']}")
                    else:
                        msgbox("Все поля для ввода обязательны!")
                if enter_add == "Нового покупателя":
                    database1 = multenterbox("Введите данные нового покупателя:", "Enter", ["Введите имя:", "Введите номер телефона:"])
                    if database1[0] and database1[1]:
                        with connection.cursor() as cursor:
                            insert = f"INSERT INTO `Customers` (name, phone) VALUES ('{database1[0]}', '{database1[1]}');"
                            cursor.execute(insert)
                            connection.commit()
                        msgbox("Информация успешно добавлена!")
                    else:
                        msgbox("Все поля для ввода обязательны!")
                if enter_add == "Новую сделку":
                    database1 = multenterbox("Введите данные сделки:\n\n(Оставить поле \"Телефон покупателя\" "
                                             "пустым если покупатель не хочет регистрироваться)", "Enter", ["ID продавца:", "Телефон покупателя:", "Название продукта:", "Сумма покупки"])
                    if database1[0] and database1[2] and database1[3]:
                        if database1[1] == "":
                            with connection.cursor() as cursor:
                                insert = f"INSERT INTO `Sales` (idSalesmen, phoneCustomers, nameProduct, summa) VALUES ('{database1[0]}', '380000000000', '{database1[2]}', {database1[3]});"
                                cursor.execute(insert)
                                connection.commit()
                            msgbox("Информация успешно добавлена!")
                        else:
                            with connection.cursor() as cursor:
                                insert = f"INSERT INTO `Sales` (idSalesmen, phoneCustomers, nameProduct, summa) VALUES ('{database1[0]}', '{database1[1]}', '{database1[2]}', {database1[3]});"
                                cursor.execute(insert)
                                connection.commit()
                            msgbox("Информация успешно добавлена!")
                    else:
                        msgbox("Все поля для ввода обязательны, кроме номера телефона покупателя!")

            elif enter == "Вывести данные":
                enter_output = buttonbox("Что выводить?\n\n1 - Все сделки\n2 - Все сделки определенного продавца\n"
                                         "3 - Максимальная сумма из всех сделок\n4 - Мин сумма из всех сделок\n"
                                         "5 - Максимальная сумма из всех сделок определенного продавца\n"
                                         "6 - Минимальная сумма из всех сделок определенного продавца\n"
                                         "7 - Максимальная сумма из всех сделок определенного покупателя\n"
                                         "8 - Минимальная сумма из всех сделок определенного покупателя\n"
                                         "9 - Продавец с максимальной суммой продажи из всех сделок\n"
                                         "10 - Продавец с минимальной суммой продажи из всех сделок\n"
                                         "11 - Покупателя с максимальной суммой покупки из всех сделок\n"
                                         "12 - Средняя сумма из всех покупок определенного продавца\n"
                                         "13 - Средняя сумма из всех продаж определенного продавца", "Choose", ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"])
                if enter_output == "1":
                    out = output_info("SELECT * FROM `sales`;")
                    if out != "-":
                        with open(out + ".txt", "w") as file:
                            for i in result:
                                file.write(f"perId: {i['perId']}\nidSalesmen: {i['idSalesmen']}\nnameSalesmen: {i['nameSalesmen']}\nphoneCustomers: {i['phoneCustomers']}\nnameProduct: {i['nameProduct']}\nsumma: {i['summa']}\n\n")
                            msgbox("Данные успешно сохранены!")
                elif enter_output == "2":
                    out = output_info(f"""SELECT * FROM `sales` WHERE idSalesmen = '{enterbox("Введите ID продавца:", "Enter")}';""")
                    if out != "-":
                        with open(out + ".txt", "w") as file:
                            for i in result:
                                file.write(f"perId: {i['perId']}\nidSalesmen: {i['idSalesmen']}\nnameSalesmen: {i['nameSalesmen']}\nphoneCustomers: {i['phoneCustomers']}\nnameProduct: {i['nameProduct']}\nsumma: {i['summa']}\n\n")
                            msgbox("Данные успешно сохранены!")
                elif enter_output == "3":
                    out = output_info("SELECT * FROM `sales` WHERE summa = (SELECT MAX(summa) FROM `sales`);")
                    if out != "-":
                        with open(out + ".txt", "w") as file:
                            for i in result:
                                file.write(f"perId: {i['perId']}\nidSalesmen: {i['idSalesmen']}\nnameSalesmen: {i['nameSalesmen']}\nphoneCustomers: {i['phoneCustomers']}\nnameProduct: {i['nameProduct']}\nsumma: {i['summa']}\n\n")
                            msgbox("Данные успешно сохранены!")
                elif enter_output == "4":
                    out = output_info("SELECT * FROM `sales` WHERE summa = (SELECT MIN(summa) FROM `sales`);")
                    if out != "-":
                        with open(out + ".txt", "w") as file:
                            for i in result:
                                file.write(f"perId: {i['perId']}\nidSalesmen: {i['idSalesmen']}\nnameSalesmen: {i['nameSalesmen']}\nphoneCustomers: {i['phoneCustomers']}\nnameProduct: {i['nameProduct']}\nsumma: {i['summa']}\n\n")
                            msgbox("Данные успешно сохранены!")
                elif enter_output == "5":
                    out = output_info(f"""SELECT * FROM `sales` WHERE summa = (SELECT MAX(summa) FROM `sales` WHERE idSalesmen = '{enterbox("Введите ID продавца:", "Enter")}');""")
                    if out != "-":
                        with open(out + ".txt", "w") as file:
                            for i in result:
                                file.write(f"perId: {i['perId']}\nidSalesmen: {i['idSalesmen']}\nnameSalesmen: {i['nameSalesmen']}\nphoneCustomers: {i['phoneCustomers']}\nnameProduct: {i['nameProduct']}\nsumma: {i['summa']}\n\n")
                            msgbox("Данные успешно сохранены!")
                elif enter_output == "6":
                    out = output_info(f"""SELECT * FROM `sales` WHERE summa = (SELECT MIN(summa) FROM `sales` WHERE idSalesmen = '{enterbox("Введите ID продавца:", "Enter")}');""")
                    if out != "-":
                        with open(out + ".txt", "w") as file:
                            for i in result:
                                file.write(f"perId: {i['perId']}\nidSalesmen: {i['idSalesmen']}\nnameSalesmen: {i['nameSalesmen']}\nphoneCustomers: {i['phoneCustomers']}\nnameProduct: {i['nameProduct']}\nsumma: {i['summa']}\n\n")
                            msgbox("Данные успешно сохранены!")
                elif enter_output == "7":
                    out = output_info(f"""SELECT * FROM `sales` WHERE summa = (SELECT MAX(summa) FROM `sales` WHERE phoneCustomers = '{enterbox("Введите номер телефона покупателя:", "Enter")}');""")
                    if out != "-":
                        with open(out + ".txt", "w") as file:
                            for i in result:
                                file.write(f"perId: {i['perId']}\nidSalesmen: {i['idSalesmen']}\nnameSalesmen: {i['nameSalesmen']}\nphoneCustomers: {i['phoneCustomers']}\nnameProduct: {i['nameProduct']}\nsumma: {i['summa']}\n\n")
                            msgbox("Данные успешно сохранены!")
                elif enter_output == "8":
                    out = output_info(f"""SELECT * FROM `sales` WHERE summa = (SELECT MIN(summa) FROM `sales` WHERE phoneCustomers = '{enterbox("Введите номер телефона покупателя:", "Enter")}');""")
                    if out != "-":
                        with open(out + ".txt", "w") as file:
                            for i in result:
                                file.write(f"perId: {i['perId']}\nidSalesmen: {i['idSalesmen']}\nnameSalesmen: {i['nameSalesmen']}\nphoneCustomers: {i['phoneCustomers']}\nnameProduct: {i['nameProduct']}\nsumma: {i['summa']}\n\n")
                            msgbox("Данные успешно сохранены!")
                elif enter_output == "9":
                    out = output_info_name("SELECT idSalesmen FROM `sales` WHERE summa = (SELECT MAX(summa) FROM `sales`);")
                    if out != "-":
                        with open(out + ".txt", "w") as file:
                            file.write(f"idSalesmen: {result[0]['idSalesmen']}")
                            msgbox("Данные успешно сохранены!")
                elif enter_output == "10":
                    out = output_info_name("SELECT idSalesmen FROM `sales` WHERE summa = (SELECT MIN(summa) FROM `sales`);")
                    if out != "-":
                        with open(out + ".txt", "w") as file:
                            file.write(f"idSalesmen: {result[0]['idSalesmen']}")
                            msgbox("Данные успешно сохранены!")
                elif enter_output == "11":
                    out = output_info_name("SELECT phoneCustomers FROM `sales` WHERE summa = (SELECT MAX(summa) FROM `sales`);")
                    if out != "-":
                        with open(out + ".txt", "w") as file:
                            file.write(f"phoneCustomers: {result[0]['phoneCustomers']}")
                            msgbox("Данные успешно сохранены!")
                elif enter_output == "12":
                    out = output_info_name(f"""SELECT AVG(summa) as summa FROM `sales` WHERE phoneCustomers = '{enterbox("Введите номер телефона покупателя:", "Enter")}';""")
                    if out != "-":
                        with open(out + ".txt", "w") as file:
                            file.write(f"summa: {result[0]['summa']}")
                            msgbox("Данные успешно сохранены!")
                elif enter_output == "13":
                    out = output_info_name(f"""SELECT AVG(summa) as summa FROM `sales` WHERE idSalesmen = '{enterbox("Введите ID продавца:", "Enter")}';""")
                    if out != "-":
                        with open(out + ".txt", "w") as file:
                            file.write(f"summa: {result[0]['summa']}")
                            msgbox("Данные успешно сохранены!")

            elif enter == "Удалить данные":
                enter_delete = buttonbox("Где хотите удалить?:", "Enter", ["Таблица работников", "Таблица покупателей", "Таблица продаж"])
                if enter_delete == "Таблица работников":
                    while True:
                        enter_delete_salesmen = enterbox("Введите ID работника, которого хотите удалить из БД:", "Enter")
                        with connection.cursor() as cursor:
                            create_table = f"SELECT * FROM `Salesmen` WHERE id = {enter_delete_salesmen};"
                            if create_table:
                                cursor.execute(create_table)
                                result_delete = cursor.fetchall()
                                accept_delete = buttonbox(f"id: {result_delete[0]['id']}\nname: {result_delete[0]['name']}\nphone: {result_delete[0]['phone']}\n", "Delete", ["Да", "Нет"])
                                if accept_delete == "Да":
                                    delete_salesmen = f"UPDATE `Salesmen` SET rem = '+' WHERE id = {enter_delete_salesmen};"
                                    cursor.execute(delete_salesmen)
                                    connection.commit()
                                    msgbox("Данные успешно удалены!")
                                    break
                            else:
                                msgbox("Данного сотрудника нет в БД!")

                elif enter_delete == "Таблица покупателей":
                    while True:
                        enter_delete_customers = enterbox("Введите номер телефона покупателя, которого хотите удалить из БД:", "Enter")
                        with connection.cursor() as cursor:
                            create_table = f"SELECT * FROM `Customers` WHERE phone = {enter_delete_customers};"
                            if create_table:
                                cursor.execute(create_table)
                                result_delete = cursor.fetchall()
                                accept_delete = buttonbox(f"id: {result_delete[0]['id']}\nname: {result_delete[0]['name']}\nphone: {result_delete[0]['phone']}\n", "Delete", ["Да", "Нет"])
                                if accept_delete == "Да":
                                    delete_customers = f"UPDATE `Customers` SET rem = '+' WHERE phone = {enter_delete_customers};"
                                    cursor.execute(delete_customers)
                                    connection.commit()
                                    msgbox("Данные успешно удалены!")
                                    break
                            else:
                                msgbox("Данного покупателя нет в БД!")

                elif enter_delete == "Таблица продаж":
                    while True:
                        enter_delete_sales = enterbox("Введите perId сделки, которую хотите удалить из БД:", "Enter")
                        with connection.cursor() as cursor:
                            create_table = f"SELECT * FROM `Sales` WHERE perId = {enter_delete_sales};"
                            if create_table:
                                cursor.execute(create_table)
                                result_delete = cursor.fetchall()
                                accept_delete = buttonbox(f"perId: {result_delete[0]['perId']}\nidSalesmen: {result_delete[0]['idSalesmen']}\nnameSalesmen: {result_delete[0]['nameSalesmen']}\nphoneCustomers: {result_delete[0]['phoneCustomers']}\nnameProduct: {result_delete[0]['nameProduct']}\nsumma: {result_delete[0]['summa']}\n", "Delete", ["Да", "Нет"])
                                if accept_delete == "Да":
                                    delete_sales = f"DELETE FROM `Sales` WHERE perId = {enter_delete_sales};"
                                    cursor.execute(delete_sales)
                                    connection.commit()
                                    msgbox("Данные успешно удалены!")
                                    break
                            else:
                                msgbox("Данной сделки нет в БД!")

            else:
                break
    finally:
        connection.close()

except:
    print("error")