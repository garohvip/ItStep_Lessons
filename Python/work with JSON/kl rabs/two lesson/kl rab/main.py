from easygui import *
import json
import os

path = os.path.join("data_base", "test1.json")

dict_var = {
    "geno": {
        "password": "qwerty",
        "mail": ["geno@gmail.com", "geno@mail.ru"]
    },
    "arbuz": {
        "password": "123456",
        "mail": ["arbuz@gmail.com", "arbuz@mail.ru"]
    }
}

while True:
    interface = buttonbox("Choose act:", "Action", ["ADD", "REMOVE", "FIND", "EDIT", "IMPORT", "DEFAULT", "EXIT"])

    if interface == "ADD":
        with open(path, "r") as file:
            dict_var_read = json.load(file)
        enter_data = multenterbox("Введите данные:", "Data", ["login", "pass", "mails"])
        dict_var_read[enter_data[0]] = {"password": enter_data[1], "mail": enter_data[2].split()}
        with open(path, "w") as file:
            json.dump(dict_var_read, file)
        msgbox(dict_var_read)

    elif interface == "REMOVE":
        with open(path, "r") as file:
            dict_var_read = json.load(file)
        login = enterbox("Введите страну которую хотите удалить: ")
        dict_var_read.pop(login)
        with open(path, "w") as file:
            json.dump(dict_var_read, file)
        msgbox(dict_var_read)

    elif interface == "FIND":
        with open(path, "r") as file:
            dict_var_read = json.load(file)
        variant = buttonbox("Выберите по чему будет поиск:", "Variant", ["LOGIN", "MAIL", "WORK"])
        msg_box = ""
        if variant == "MAIL":
            enter_key = multenterbox("Введите данные", "Enter", ["postmail"])
            msgbox("\n".join([f'login: {i}, password: {dict_var_read.get(i).get("password")}, mail: {", ".join(dict_var_read.get(i).get("mail"))}' for i in dict_var_read if enter_key[0] in dict_var_read.get(i)["mail"]]))
        elif variant == "LOGIN":
            enter_key = multenterbox("Введите данные", "Enter", ["loginuser"])
            # msgbox("\n".join([f'login: {i}, password: {dict_var_read.get(i).get("password")}, mail: {", ".join(dict_var_read.get(i).get("mail"))}' for i in dict_var_read if enter_key[0] in dict_var_read]))
            kk = dict_var_read.keys()
            for i in range(len(kk)):
                if enter_key[0] == kk[i]:
                    msg_box = msg_box + f"login: {i} password: {dict_var_read.get(i).get('password')} mail: {', '.join(dict_var_read.get(i).get('mail'))}\n"
            msgbox(msg_box)

    elif interface == "EDIT":
        with open(path, "r") as file:
            dict_var_read = json.load(file)
        enter_edit = buttonbox("Что хотите редактировать?", "Редакция", ["COUNTRY", "CAPITAL"])
        if enter_edit == "COUNTRY":
            enter_old_login = enterbox("Введите название старой страны: ")
            enter_new_login = enterbox("Введите название новой страны: ")
            dict_var_read[enter_new_login] = dict_var_read.pop(enter_old_login)
        elif enter_edit == "CAPITAL":
            enter_login = enterbox("Введите название страны: ")
            enter_new_password = enterbox("Введите новую столицу: ")
            dict_var_read[enter_login] = enter_new_password
        with open(path, "w") as file:
            json.dump(dict_var_read, file)
        msgbox(dict_var_read)

    elif interface == "IMPORT":
        with open(path, "r") as file:
            dict_var_read = json.load(file)
        msgbox(dict_var_read)

    elif interface == "DEFAULT":
        with open(path, "w") as file:
            json.dump(dict_var, file)
        msgbox("Таблица вернута к данным по умолчанию")

    else:
        break