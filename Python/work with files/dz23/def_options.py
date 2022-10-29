import json

# ------------ OUTPUT INFO -------------


def output_all(path_to_file):  # функция вывода ВСЕХ ПОЛЬЗОВАТЕЛЕЙ
    with open(path_to_file, "r") as file:
        read_file = json.load(file)
    var_output = []
    for i in read_file:
        var_output.append(f"Name: {i}\nAge: {read_file[i]['Age']}\nWork: {read_file[i]['Work']}\n")
    return var_output


def write_add_to_file(path_file_to_file, var_e_var,
                      var_output_var):  # функция добавление или перезаписи ТЕКСТОВОГО файла
    if var_e_var == "ADD":
        with open(path_file_to_file, "a") as file:
            return file.write("".join(var_output_var))
    elif var_e_var == "REWRITE":
        with open(path_file_to_file, "w") as file:
            return file.write("".join(var_output_var))


def output_find(path_to_file, find_name_var):  # функция поиска по NAME
    with open(path_to_file, "r") as file:
        read_file = json.load(file)
    var_output = []
    for i in read_file:
        if i == find_name_var.title():
            var_output.append(f"Name: {i}\nAge: {read_file[i]['Age']}\nWork: {read_file[i]['Work']}\n")
    return var_output


def output_first_name_symbol(path_to_file, find_first_name_sym_var):  # функция поиска по FIRST NAME SYMBOL
    with open(path_to_file, "r") as file:
        read_file = json.load(file)
    var_output = []
    for i in read_file:
        if i[0] == find_first_name_sym_var.title():
            var_output.append(f"Name: {i}\nAge: {read_file[i]['Age']}\nWork: {read_file[i]['Work']}\n")
    return var_output


def output_age_work(path_to_file, find_age_work_var, age_or_work=""):  # функция поиска по AGE or WORK
    with open(path_to_file, "r") as file:
        read_file = json.load(file)
    var_output = []
    for i in read_file:
        if read_file[i][age_or_work].lower() == find_age_work_var.lower():
            var_output.append(f"Name: {i}\nAge: {read_file[i]['Age']}\nWork: {read_file[i]['Work']}\n")
    return var_output


# ----------- ADD INFO ------------


def add_data(path_to_file, var_add_var):  # Добавить в базу человека
    with open(path_to_file, "r") as file:
        read_file = json.load(file)
    read_file[var_add_var[0].title()] = {"Age": var_add_var[1], "Work": var_add_var[2].title()}
    with open(path_to_file, "w") as file:
        json.dump(read_file, file)
    return f"{var_add_var[0].title()} успешно добавлен в базу!"


# ------------ REMOVE INFO ---------------


def remove_data(path_to_file, var_remove_var):  # Удалить из базы человека
    counting = 0
    with open(path_to_file, "r") as file:
        read_file = json.load(file)
    for i in read_file:
        if i == var_remove_var.title():
            read_file.pop("".join(i))
            with open(path_to_file, "w") as file:
                json.dump(read_file, file)
            return f"{''.join(i)} успешно удалено из базы данных."
    if counting == 0:
        return f"{var_remove_var.title()} is not found!"
