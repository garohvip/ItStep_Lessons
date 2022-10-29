import json
import os
from easygui import *

path = os.path.join("data_base", "base.json")

dict_var = {
    "Gregor Vanhelsing": {
        "Age": "20",
        "Work": "Student"
    },
    "Max Osipov": {
        "Age": "32",
        "Work": "Gangster"
    }
}

while True:
    interface = buttonbox("Choose action:", "Actions", ["ADD/EDIT", "REMOVE", "FIND", "IMPORT", "ENTER", "EXIT"])

    if interface == "ADD/EDIT":
        with open(path, "r") as file:
            dict_var_read = json.load(file)
        data = multenterbox("Enter data", "Employer", ["Name", "Age", "Work"])
        dict_var_read[data[0]] = {"Age": data[1], "Work": data[2]}
        with open(path, "w") as file:
            json.dump(dict_var_read, file)
        msgbox("Данные успешно добавлены", "Успех")

    elif interface == "REMOVE":
        with open(path, "r") as file:
            dict_var_read = json.load(file)
        login = enterbox("Введите имя пользователя которого хотите удалить: ")
        dict_var_read.pop(login)
        with open(path, "w") as file:
            json.dump(dict_var_read, file)
        msgbox("Данные успешно добавлены", "Успех")

    elif interface == "FIND":
        with open(path, "r") as file:
            dict_var_read = json.load(file)
        variant = buttonbox("Выберите по чему будет поиск:", "Variant", ["NAME", "AGE", "WORK"])
        msg_box = ""
        if variant == "AGE":
            enter_key = multenterbox("Введите данные", "Enter", ["Number"])
            msgbox("\n".join([f'Name: {i}, Age: {dict_var_read.get(i).get("Age")}, Work: {dict_var_read.get(i).get("Work")}' for i in dict_var_read if enter_key[0] == dict_var_read.get(i)["Age"]]))
            # for i in dict_var_read:
            #     if enter_key[0] == dict_var_read.get(i)['Age']:
            #         msg_box = msg_box + f"Name: {i} Age: {dict_var_read.get(i).get('Age')} Work: {dict_var_read.get(i).get('Work')}\n"
        elif variant == "NAME":
            enter_key = multenterbox("Введите данные", "Enter", ["NameSurname"])
            msgbox("\n".join([f'Name: {i}, Age: {dict_var_read.get(i).get("Age")}, Work: {dict_var_read.get(i).get("Work")}' for i in dict_var_read if enter_key[0] == dict_var_read["Name"]]))
    # elif interface == "EDIT":
    #     pass
        # with open(path, "r") as file:
        #     dict_var_read = json.load(file)
        # enter_edit = input("Что хотите редактировать?: log/pass ")
        # if enter_edit == "log":
        #     enter_old_login = input("Введите старый логин: ")
        #     enter_new_login = input("Введите новый логин: ")
        #     dict_var_read[enter_new_login] = dict_var_read.pop(enter_old_login)
        # elif enter_edit == "pass":
        #     enter_login = input("Введите логин: ")
        #     enter_new_password = input("Введите новый пароль: ")
        #     dict_var_read[enter_login] = enter_new_password
        # with open(path, "w") as file:
        #     json.dump(dict_var_read, file)

    elif interface == "IMPORT":
        with open(path, "r") as file:
            dict_var_read = json.load(file)
        msgbox(dict_var_read, "Данные")

    elif interface == "ENTER":
        with open(path, "w") as file:
            json.dump(dict_var, file)
        msgbox("Данные успешно обновлены до начальных", "Успех")
    else:
        break