import pymysql
import base64

def basePhoto(path):
    with open(path, "rb") as file:
        base_64 = base64.b64encode(file.read()).decode('utf-8')
    return base_64

try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user='root',
        password='DataBase0321',
        database='django_one',
        cursorclass=pymysql.cursors.DictCursor
    )
    # with connection.cursor() as cursor:
    #     create_table = "CREATE TABLE `table` (id INT AUTO_INCREMENT, nameBook varchar(30), yearCreate DATE, author varchar(30), style varchar(30), vidavnitstvo varchar(30), available BOOL, images MEDIUMTEXT, PRIMARY KEY (id));"
    #     cursor.execute(create_table)
    with connection.cursor() as cursor:
        create_table = f"""INSERT INTO `table` (nameBook, yearCreate, author, style, vidavnitstvo, available, images) VALUES ('Тысячеликий герой', '1949-01-01', 'Джозеф Кэмпбелл', 'Наука', 'София', 1, '{basePhoto("images/1000hero.jpg")}')"""
        cursor.execute(create_table)
        connection.commit()
except Exception as ex:
    print(ex)
