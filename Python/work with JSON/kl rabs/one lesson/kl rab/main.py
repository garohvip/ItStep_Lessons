import json
import os.path

path = os.path.join("data_base", "test1.json")


# dict_var = {
#     1: "Nosachenko",
#     "Max":  "Babaev",
#     "Sasha": "Ozerov"
# }



while True:
    print(f"0 - Выход\n1 - Загрузка данных\n2 - Выгрузка данных\n3 - Добавление данных\n4 - Удаление данных")
    user_enter = int(input("Выберите пункт: "))
    if user_enter == 1:
        with open(path, "w") as file:
            list_var = [int(i) for i in input("Введите данные в ряд: ").split()]
            json.dump(list_var, file) # Для записи данных (сериализации)

    elif user_enter == 2:
        with open(path, "r") as file:
            dict_var = json.load(file) # Для вывода данных (десериализация)
            print(f"Вывод данных с JSON: {dict_var}")

    elif user_enter == 3:
        with open(path, "r") as file1:
            dict_var = json.load(file1)
        dict_var = dict_var + [int(i) for i in input("Enter number: ").split()]
        with open(path, "w") as file2:
            json.dump(list_var, file2)

    elif user_enter == 4:
        with open(path, "r") as file1:
            dict_var = json.load(file1)
        delete_numbers = int(input("Сколько хотите удалить данных: "))
        for i in range(delete_numbers):
            print(f"Данные сейчас: {dict_var}")
            delete_number = int(input("Какое число хотите удалить из списка?: "))
            dict_var.remove(delete_number)
        with open(path, "w") as file2:
            json.dump(dict_var, file2)

    elif user_enter == 0:
        break