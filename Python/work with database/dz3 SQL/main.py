import pymysql
from easygui import *

with open("pass.txt", "r") as file:
    pw = file.read()
try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password=pw,
        database="sakila2",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Welcome to the database")
    try:
        while True:
            enter = buttonbox("Choise:", "Choose", ["Создать таблицу", "Добавить данные", "Вывести данные", "Удалить данные"])
            if enter == "Создать таблицу":
                with connection.cursor() as cursor:
                    create_table = "CREATE TABLE `people` (id INT AUTO_INCREMENT," \
                                   "name varchar(30)," \
                                   "surname varchar(30)," \
                                   "country varchar(20)," \
                                   "city varchar(20)," \
                                   "birthday varchar(10)," \
                                   "PRIMARY KEY (id));"
                    cursor.execute(create_table)
                    print("Successes!")

            elif enter == "Добавить данные":
                database1 = multenterbox("Enter:", "Enter", ["Введите имя:", "Введите фамилию:", "Введите страну:", "Введите город:", "Введите дату рождения:"])
                print(database1)
                with connection.cursor() as cursor:
                    insert = f"INSERT INTO `people` (name, surname, country, city, birthday) VALUES ('{database1[0]}', '{database1[1]}', '{database1[2]}', '{database1[3]}', '{database1[4]}')"
                    cursor.execute(insert)
                    connection.commit()

            elif enter == "Вывести данные":
                with connection.cursor() as cursor:
                    create_table = "SELECT * FROM `people`"
                    cursor.execute(create_table)
                    result = cursor.fetchall()
                    msgbox(result)

            elif enter == "Удалить данные":
                pass

            else:
                break

        # DROPS TABLE ??
        # with connection.cursor() as cursor:
        #     create_table = "DROP TABLE `students`"
        #     cursor.execute(create_table)

        # with connection.cursor() as cursor:
        #     create_table = "DELETE FROM `students` WHERE id=2;"
        #     cursor.execute(create_table)
        #     connection.commit()

        # UPDATE DATA
        # with connection.cursor() as cursor:
        #     create_table = "UPDATE `students` SET password = 'qwer' WHERE id = 1"
        #     cursor.execute(create_table)
        #     connection.commit()
    finally:
        connection.close()

except:
    print("error brooo!!")