import json
import os

path = os.path.join("data_base", "base.json")

dict_var = {
    "Украина": "Киев",
    "Великобритания": "Лондон",
    "Польша": "Варшава",
    "США": "Вашингтон",
    "Мексика": "Мехико",
    "Китай": "Пекин"
}

while True:
    print("0 - Exit | 1 - Add | 2 - Remove | 3 - Find | 4 - Edit | 5 - Import | 6 - Enter")
    enter_user = input()
    if enter_user == "0":
        break

    elif enter_user == "1":
        with open(path, "r") as file:
            dict_var_read = json.load(file)
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        dict_var_read[login] = password
        with open(path, "w") as file:
            json.dump(dict_var_read, file)
        print(dict_var_read)

    elif enter_user == "2":
        with open(path, "r") as file:
            dict_var_read = json.load(file)
        login = input("Введите ник пользователя которого хотите удалить: ")
        dict_var_read.pop(login)
        with open(path, "w") as file:
            json.dump(dict_var_read, file)
        print(dict_var_read)

    elif enter_user == "3":
        with open(path, "r") as file:
            dict_var_read = json.load(file)
        enter_find_key = input("Введите ключ, который хотите найти: ")
        find_key = dict_var_read.get(enter_find_key)
        print(f"login: {enter_find_key} password: {find_key}")

    elif enter_user == "4":
        with open(path, "r") as file:
            dict_var_read = json.load(file)
        enter_edit = input("Что хотите редактировать?: log/pass ")
        if enter_edit == "log":
            enter_old_login = input("Введите старый логин: ")
            enter_new_login = input("Введите новый логин: ")
            dict_var_read[enter_new_login] = dict_var_read.pop(enter_old_login)
        elif enter_edit == "pass":
            enter_login = input("Введите логин: ")
            enter_new_password = input("Введите новый пароль: ")
            dict_var_read[enter_login] = enter_new_password
        with open(path, "w") as file:
            json.dump(dict_var_read, file)

    elif enter_user == "5":
        with open(path, "r") as file:
            dict_var_read = json.load(file)
        print(dict_var_read)

    elif enter_user == "6":
        with open(path, "w") as file:
            json.dump(dict_var, file)
        print("Добавлено")