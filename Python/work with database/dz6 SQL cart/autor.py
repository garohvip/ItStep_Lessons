def authorization(login, password, connection):
    with connection.cursor() as cursor:
        if cursor.execute(f"""SELECT name FROM `users` WHERE login = '{login.lower()}' AND password = '{password}'"""):
            return True
        else:
            return False


def registration(login, password, name, connection):
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT login FROM `users` WHERE login = '{login}'""")
        zp = cursor.fetchone()
    if zp:
        return "Данный пользователь уже зарегестрирован!"
    else:
        with connection.cursor() as cursor:
            cursor.execute(f"""INSERT INTO `users` (login, password, name) VALUES ('{login.lower()}', '{password}', '{name}');""")
            connection.commit()
        return "Успешная регистрация!"