import pymysql

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
    finally:
        connection.close()
except:
    print("Error")
