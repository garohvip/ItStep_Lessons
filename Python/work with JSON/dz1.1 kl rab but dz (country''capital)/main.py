from easygui import *
import json
import os

path = os.path.join("data_base", "test1.json")

dict_var = {
    "Ukraine": "Kyiv",
    "Great Britain": "London",
    "Poland": "Warsaw"
}

while True:
    interface = buttonbox("Choose act:", "Action", ["ADD", "REMOVE", "FIND", "EDIT", "IMPORT ALL", "DEFAULT", "EXIT"])

    if interface == "ADD":
        with open(path, "r") as file:
            dict_var_read = json.load(file)
        country = enterbox("Enter country:")
        capital = enterbox(f"Enter capital {country.title()}")
        dict_var_read[country.title()] = capital.title()
        with open(path, "w") as file:
            json.dump(dict_var_read, file)
        msgbox(f"Country: {country.title()}\nCapital: {capital.title()}\nSuccessfully added to the database!")

    elif interface == "REMOVE":
        remove_interface = buttonbox("Choose what you want to delete?", "Delete", ["COUNTRY", "CAPITAL", "ALL"])
        if remove_interface == "COUNTRY":
            with open(path, "r") as file:
                dict_var_read = json.load(file)
            country = enterbox("Enter the country you want to delete:")
            dict_var_read.pop(country.title())
            with open(path, "w") as file:
                json.dump(dict_var_read, file)
            msgbox(f"Country {country.title()}\nSuccessfully delete from database!")
        elif remove_interface == "CAPITAL":
            with open(path, "r") as file:
                dict_var_read = json.load(file)
            capital = enterbox("Enter the capital you want to delete:")
            for i in dict_var_read:
                if dict_var_read[i] == capital.title():
                    dict_var_read.pop(i)
                    break
            with open(path, "w") as file:
                json.dump(dict_var_read, file)
            msgbox(f"Capital {capital.title()}\nSuccessfully delete from database!")
        elif remove_interface == "ALL":
            new_dict_var = {}
            with open(path, "w") as file:
                json.dump(new_dict_var, file)
            msgbox("Database successfully cleared!")

    elif interface == "FIND":
        find_interface = buttonbox("What parameter do you want to search for?", "Find", ["COUNTRY", "CAPITAL"])
        if find_interface == "COUNTRY":
            with open(path, "r") as file:
                dict_var_read = json.load(file)
            enter_find_key = enterbox("Enter the country name you want to find: ")
            find_key = dict_var_read[enter_find_key.title()]
            msgbox(f"Country: {enter_find_key.title()}\nCapital: {find_key}")
        elif find_interface == "CAPITAL":
            with open(path, "r") as file:
                dict_var_read = json.load(file)
            enter_find_value = enterbox("Enter the capital name you want to find:")
            for i in dict_var_read:
                if dict_var_read[i] == enter_find_value.title():
                    msgbox(f"Country: {i}\nCapital: {dict_var_read[i]}")
                    break

    elif interface == "EDIT":
        with open(path, "r") as file:
            dict_var_read = json.load(file)
        enter_edit = buttonbox("What do you want to edit?", "Editor", ["COUNTRY", "CAPITAL"])
        if enter_edit == "COUNTRY":
            enter_old_country = enterbox("Enter the name of the old country: ")
            enter_new_country = enterbox("Enter the name of the new country: ")
            dict_var_read[enter_new_country.title()] = dict_var_read.pop(enter_old_country.title())
        elif enter_edit == "CAPITAL":
            enter_country = enterbox("Enter country: ")
            enter_new_capital = enterbox("Enter new capital: ")
            dict_var_read[enter_country.title()] = enter_new_capital.title()
        with open(path, "w") as file:
            json.dump(dict_var_read, file)
        msgbox(f"The changes have been successfully implemented!")

    elif interface == "IMPORT ALL":
        with open(path, "r") as file:
            dict_var_read = json.load(file)
        all_info = []
        for i in dict_var_read:
            all_info.append(f"Country: {i}\nCapital: {dict_var_read[i]}\n")
        msgbox("\n".join(all_info))

    elif interface == "DEFAULT":
        with open(path, "w") as file:
            json.dump(dict_var, file)
        msgbox("Table returned to default data")

    else:
        break