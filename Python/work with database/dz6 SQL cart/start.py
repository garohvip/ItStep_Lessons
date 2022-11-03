def start(connection):
    with connection.cursor() as cursor:
        create_table = "CREATE TABLE `users` (idUsers INT AUTO_INCREMENT, name varchar(13), login varchar(30) UNIQUE, password varchar(30), PRIMARY KEY (idUsers));"
        cursor.execute(create_table)
        create_table = "CREATE TABLE `products` (idProd INT AUTO_INCREMENT, nameProduct varchar(30) UNIQUE, price INT, PRIMARY KEY (idProd));"
        cursor.execute(create_table)
        create_table = "CREATE TABLE `cart` (idCart INT AUTO_INCREMENT, loginUser varchar(30), nameProduct varchar(30)," \
                       " count INT, price INT, PRIMARY KEY (idCart), FOREIGN KEY (nameProduct) REFERENCES products(nameProduct), " \
                       "FOREIGN KEY (loginUser) REFERENCES users(login));"
        cursor.execute(create_table)