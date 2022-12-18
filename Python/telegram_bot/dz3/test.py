import pymysql
try:
    connection = pymysql.connect(
            host="localhost",
            port=3306,
            user='root',
            password='DataBase0321',
            database='shop_cart_telegram',
            cursorclass=pymysql.cursors.DictCursor
        )
    with connection.cursor() as cursor:
        cursor.execute(f"""CREATE TABLE `cartUser` (idUser INT AUTO_INCREMENT, 
        idTelegramUser BIGINT, nameProd varchar(100) DEFAULT NULL, nameCategories varchar(100),
          value INT DEFAULT NULL, price INT DEFAULT NULL, FOREIGN KEY(nameCategories) REFERENCES categories(nameCategories), PRIMARY KEY (idUser));""")

except:
    print("error")