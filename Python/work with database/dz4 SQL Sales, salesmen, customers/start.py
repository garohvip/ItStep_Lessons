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
        database="sales",
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        with connection.cursor() as cursor:
            create_table = "CREATE TABLE `Salesmen` (id INT AUTO_INCREMENT, name varchar(30), phone varchar(13), rem varchar(1) DEFAULT '-', PRIMARY KEY (id));"
            cursor.execute(create_table)
            create_table = "CREATE TABLE `Customers` (id INT AUTO_INCREMENT, phone varchar(13) UNIQUE, name varchar(30), rem varchar(1) DEFAULT '-', PRIMARY KEY (id));"
            cursor.execute(create_table)
            create_table = "CREATE TABLE `Sales` (perId INT AUTO_INCREMENT, " \
                           "idSalesmen INT, nameSalesmen varchar(30) DEFAULT 'подтянуть с другой табл', phoneCustomers varchar(13), " \
                           "nameProduct varchar(30), summa INT, PRIMARY KEY (perId), " \
                           "FOREIGN KEY (idSalesmen) REFERENCES Salesmen(id), " \
                           "FOREIGN KEY (phoneCustomers) REFERENCES Customers(phone));"
            cursor.execute(create_table)
        # with connection.cursor() as cursor:
        #     insert = "INSERT INTO `Salesmen` (name, phone) VALUES ('Sasha', '380961234567'), ('Max', '380689876543');"
        #     cursor.execute(insert)
        #     insert = "INSERT INTO `Customers` (phone, name) VALUES ('380989999999', 'Kolya'), ('380981111111', 'Andrey');"
        #     cursor.execute(insert)
        #     insert = "INSERT INTO `Sales` (idSalesmen, phoneCustomers, nameProduct, summa) VALUES ('2', '380989999999', 'Door', 1000);"
        #     cursor.execute(insert)
        #     connection.commit()
    finally:
        connection.close()
except Exception as ex:
    print(ex)