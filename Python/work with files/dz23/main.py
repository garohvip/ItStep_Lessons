from def_options import *
import os.path
from easygui import *

path = os.path.join("jsonfile.json")
path_file = os.path.join("info_user_from_search.txt")

while True:
    interface = buttonbox("Select an action:", "Menu", ["ADD", "REMOVE", "EDIT", "OUTPUT", "EXIT"])

    if interface == "ADD":
        var_a = multenterbox("Enter user information: (Name Surname)", "Add new user", ["Surname Name:", "Age:", "Work:"])
        msgbox(add_data(path, var_a))

    elif interface == "REMOVE":
        var_a = enterbox("Enter surname and name user whom you want is delete: (Name Surname)")
        msgbox(remove_data(path, var_a))

    elif interface == "EDIT":
        while True:
            var_a = enterbox("Enter surname and name user whom you want is edit: (Name Surname)")
            with open(path, "r") as file:
                read_file = json.load(file)
            count = 1
            for i in read_file:
                if i == var_a.title():
                    var_b = buttonbox(f"{''.join(i)}\nЧто хотите изменить?", "Edit", ["NAME", "AGE", "WORK", "ALL"])
                    if var_b == "NAME":
                        var_new_date = enterbox("Enter new name of user: (Name Surname)", "Edit")
                        read_file[var_new_date.title()] = read_file.pop(i)
                        msgbox("Name successfully changed!")
                        count = 0
                        break
                    elif var_b == "AGE":
                        var_new_date = enterbox("Enter new age of user:", "Edit")
                        read_file[i]["Age"] = var_new_date
                        msgbox("Age successfully changed!")
                        count = 0
                        break
                    elif var_b == "WORK":
                        var_new_date = enterbox("Enter new work of user:", "Edit")
                        read_file[i]["Work"] = var_new_date.capitalize()
                        msgbox("Work successfully changed!")
                        count = 0
                        break
                    elif var_b == "ALL":
                        var_all_info = multenterbox("Enter new info about user: (Name Surname)", "Edit", ["NAME:", "AGE:", "WORK:"])
                        read_file[i]["Age"] = var_all_info[1]
                        read_file[i]["Work"] = var_all_info[2].capitalize()
                        read_file[var_all_info[0].title()] = read_file.pop(i)
                        msgbox("All info successfully changed!")
                        count = 0
                        break
            if count == 1:
                msgbox(f"User {var_a.title()} is not found!")

            with open(path, "w") as file:
                json.dump(read_file, file)
            break

    elif interface == "OUTPUT":
        var_a = buttonbox("What search do you choose:", "Output", ["FIND", "ALL"])
        if var_a == "FIND":
            var_b = buttonbox("By which option to search:", "Output", ["NAME", "FIRST NAME SYMBOL", "AGE", "WORK"])
            if var_b == "NAME":
                find_name = enterbox("Enter name of user: (Name Surname)", "Name search")
                var_output_list = output_find(path, find_name)
                if var_output_list:
                    var_c = buttonbox("\n".join(var_output_list), "FIND", ["ADD TO FILE", "GO TO MENU"])
                    if var_c == "ADD TO FILE":
                        var_e = buttonbox("Add data or overwrite:", "ADD TO FILE", ["ADD", "REWRITE"])
                        write_add_to_file(path_file, var_e, var_output_list)
                        msgbox("User successfully added to file!")
                else:
                    msgbox("User is not found!")

            elif var_b == "FIRST NAME SYMBOL":
                find_age = enterbox("Enter first name symbol of user: (Only 1 symbol)", "First name symbol search")
                var_output_list = output_first_name_symbol(path, find_age)
                if var_output_list:
                    var_c = buttonbox("\n".join(var_output_list), "First name symbol search", ["ADD TO FILE",
                                                                                               "GO TO MENU"])
                    if var_c == "ADD TO FILE":
                        var_e = buttonbox("Add data or overwrite:", "ADD TO FILE", ["ADD", "REWRITE"])
                        write_add_to_file(path_file, var_e, var_output_list)
                        msgbox("User successfully added to file!")
                else:
                    msgbox("User is not found!")

            elif var_b == "AGE":
                find_age = enterbox("Enter age of user:", "Age search")
                var_output_list = output_age_work(path, find_age, age_or_work="Age")
                if var_output_list:
                    var_c = buttonbox("\n".join(var_output_list), "First name symbol search", ["ADD TO FILE",
                                                                                               "GO TO MENU"])
                    if var_c == "ADD TO FILE":
                        var_e = buttonbox("Add data or overwrite:", "ADD TO FILE", ["ADD", "REWRITE"])
                        write_add_to_file(path_file, var_e, var_output_list)
                        msgbox("User successfully added to file!")
                else:
                    msgbox("User is not found!")

            elif var_b == "WORK":
                find_age = enterbox("Enter work of user:", "Work search")
                var_output_list = output_age_work(path, find_age, age_or_work="Work")
                if var_output_list:
                    var_c = buttonbox("\n".join(var_output_list), "First name symbol search", ["ADD TO FILE",
                                                                                               "GO TO MENU"])
                    if var_c == "ADD TO FILE":
                        var_e = buttonbox("Add data or overwrite:", "ADD TO FILE", ["ADD", "REWRITE"])
                        write_add_to_file(path_file, var_e, var_output_list)
                        msgbox("User successfully added to file!")
                else:
                    msgbox("User is not found!")

        elif var_a == "ALL":
            var_output_list = output_all(path)
            if var_output_list:
                var_c = buttonbox("\n".join(var_output_list), "First name symbol search", ["ADD TO FILE", "GO TO MENU"])
                if var_c == "ADD TO FILE":
                    var_e = buttonbox("Add data or overwrite:", "ADD TO FILE", ["ADD", "REWRITE"])
                    write_add_to_file(path_file, var_e, var_output_list)
            else:
                msgbox("The user list is empty!")

    else:
        break
