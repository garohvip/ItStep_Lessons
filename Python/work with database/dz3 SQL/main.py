import pymysql
from config import *

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Welcome to the database")
    # try:
    #
    # finally:
    #     connection.close()

except Exception as ex:
    print(ex)
