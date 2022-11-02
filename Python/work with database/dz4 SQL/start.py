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
            new_table = """CREATE TABLE `peoples` (id INT AUTO_INCREMENT, name varchar(30), surname varchar(30), city varchar(30), country varchar(30), birthday DATE, rem varchar(1) DEFAULT '-', PRIMARY KEY (id))"""
            cursor.execute(new_table)
    finally:
        connection.close()
except:
    print("error")