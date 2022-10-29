from easygui import *
import json
import os

path = os.path.join("data_base", "test1.json")

dict_var = {
    "The Beatles": {"performer": ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"], "albom": ["Please Please Me", "With the Beatles", "A Hard Day's Night", "Beatles For Sale", "Help!"]},
    "Nana": {"performer": ["Kwawe"], "albom": ["Nana", "Father", "All Doors in Flight No. 7"]}
}

while True:
    interface = buttonbox("Choose act:", "Action", ["ADD", "REMOVE", "FIND", "EDIT", "IMPORT", "DEFAULT", "EXIT"])

    if interface == "ADD":
        add_interface = buttonbox("What do you want to say?", "Add", ["GROUP", "PERFORMER IN GROUP", "ALBOM IN GROUP"])
        count = 0
        with open(path, "r") as file:
            dict_var_read = json.load(file)
        if add_interface == "GROUP":
            name_of_group = enterbox("Enter a group name:")
            name_of_performers = multenterbox("Enter the artist(s)", "Input", ["1:", "2:", "3:", "4:", "5:", "6:", "7:", "8:", "9:", "10:"])
            name_of_performers = list(filter(None, name_of_performers))
            name_of_alboms = multenterbox("Enter the album name(s)", "Input", ["1:", "2:", "3:", "4:", "5:", "6:", "7:", "8:", "9:", "10:"])
            name_of_alboms = list(filter(None, name_of_alboms))
            for i in range(len(name_of_performers)):
                name_of_performers[i] = name_of_performers[i].title()
            for i in range(len(name_of_alboms)):
                name_of_alboms[i] = name_of_alboms[i].title()
            dict_var_read[name_of_group.title()] = {"performer": name_of_performers, "albom": name_of_alboms}
            with open(path, "w") as file:
                json.dump(dict_var_read, file)
            msgbox("Successfully entered data!")

        elif add_interface == "PERFORMER IN GROUP":
            name_of_group = enterbox("Enter the name of the group where you want to add the artist:", "Add")
            for i in dict_var_read[name_of_group.title()]["performer"]:
                count += 1
            if count > 10:
                msgbox("The limit for adding artists has been exceeded!")
            else:
                name_of_performers = enterbox("Enter the name of the artist:", "Add")
                dict_var_read[name_of_group.title()]["performer"].append(name_of_performers.title())
                with open(path, "w") as file:
                    json.dump(dict_var_read, file)
                msgbox("Successfully entered data!")

        elif add_interface == "ALBOM IN GROUP":
            name_of_group = enterbox("Enter the name of the group where you want to add the album:", "Add")
            for i in dict_var_read[name_of_group.title()]["albom"]:
                count += 1
            if count > 10:
                msgbox("Album add limit has been exceeded!")
            else:
                name_of_performers = enterbox("Enter the album name:", "Add")
                dict_var_read[name_of_group.title()]["albom"].append(name_of_performers.title())
                with open(path, "w") as file:
                    json.dump(dict_var_read, file)
                msgbox("Successfully entered data!")

    elif interface == "REMOVE":
        with open(path, "r") as file:
            dict_var_read = json.load(file)
        remove_interface = buttonbox("Choose what you want to delete:", "Delete", ["GROUP", "PERFORMER", "ALBOM"])

        if remove_interface == "GROUP":
            del_group = enterbox("Enter a group name:", "Delete")
            dict_var_read.pop(del_group.title())

        elif remove_interface == "PERFORMER":
            del_performer_group = enterbox("Enter the name of the group where you want to remove the artist:", "Delete")
            del_performer = multenterbox("Enter performers:", "Delete", ["1:", "2:", "3:", "4:", "5:", "6:", "7:", "8:", "9:", "10:"])
            del_performer = list(filter(None, del_performer))
            for i in range(len(del_performer)):
                del_performer[i] = del_performer[i].title()
            for i in dict_var_read[del_performer_group.title()]["performer"]:
                for j in del_performer:
                    if i == j:
                        dict_var_read[del_performer_group.title()]["performer"].remove(j)
                        break

        elif remove_interface == "ALBOM":
            del_albom_group = enterbox("Enter the name of the group where you want to delete the album from:", "Delete")
            del_albom = multenterbox("Enter the title(s) of the album(s):", "Delete", ["1:", "2:", "3:", "4:", "5:", "6:", "7:", "8:", "9:", "10:"])
            del_albom = list(filter(None, del_albom))
            for i in range(len(del_albom)):
                del_albom[i] = del_albom[i].title()
            for i in dict_var_read[del_albom_group.title()]["albom"]:
                for j in del_albom:
                    if i == j:
                        dict_var_read[del_albom_group.title()]["albom"].remove(j)
                        break

        with open(path, "w") as file:
            json.dump(dict_var_read, file)
        msgbox("Successfully delete data!")

    elif interface == "FIND":
        find_interface = buttonbox("Выберите, что хотите найти:", "Find", ["GROUP", "PERFORMER", "ALBOM"])
        all_import = []
        count = 0
        count_all = 0
        with open(path, "r") as file:
            dict_var_read = json.load(file)

        if find_interface == "GROUP":
            find_group = enterbox("Enter a group name:", "Find")
            for i in dict_var_read:
                count_all += 1
                if i != find_group.title():
                    count += 1
                else:
                    performer_import = []
                    albom_import = []
                    for j in dict_var_read[find_group.title()]["performer"]:
                        performer_import.append(j + '\n')
                    for j in dict_var_read[find_group.title()]["albom"]:
                        albom_import.append(j + '\n')
                    msgbox(f"Group: {i}\n\nPerformer(s):\n\n{''.join(performer_import)}\nAlbom(s):\n\n{''.join(albom_import)}\n")
                    break
            if count_all == count:
                msgbox(f"{find_group.title()} group not found!")

        elif find_interface == "PERFORMER":
            var_find = []
            all_import = []
            find_performer = enterbox("Enter a performer name and surname:", "Find")
            for i in dict_var_read:
                for j in dict_var_read[i]["performer"]:
                    if j == find_performer.title():
                        var_find.append(i)
            if var_find:
                for i in var_find:
                    performer_import = []
                    albom_import = []
                    for j in dict_var_read[i]["performer"]:
                        performer_import.append(j + '\n')
                    for j in dict_var_read[i]["albom"]:
                        albom_import.append(j + '\n')
                    all_import.append(f"Group: {i}\n\nPerformer(s):\n\n{''.join(performer_import)}\nAlbom(s):\n\n{''.join(albom_import)}\n")
                msgbox("".join(all_import))
            else:
                msgbox(f"{find_performer.title()} performer not found!")

        elif find_interface == "ALBOM":
            var_find = []
            all_import = []
            find_performer = enterbox("Enter the albom:", "Find")
            for i in dict_var_read:
                for j in dict_var_read[i]["albom"]:
                    if j == find_performer.title():
                        var_find.append(i)
            if var_find:
                for i in var_find:
                    performer_import = []
                    albom_import = []
                    for j in dict_var_read[i]["performer"]:
                        performer_import.append(j + '\n')
                    for j in dict_var_read[i]["albom"]:
                        albom_import.append(j + '\n')
                    all_import.append(f"Group: {i}\n\nPerformer(s):\n\n{''.join(performer_import)}\nAlbom(s):\n\n{''.join(albom_import)}\n")
                msgbox("".join(all_import))
            else:
                msgbox(f"{find_performer.title()} albom not found!")

    elif interface == "EDIT":
        count = 0
        count_all = 0
        with open(path, "r") as file:
            dict_var_read = json.load(file)
        enter_edit = buttonbox("What do you want to edit?", "Edit", ["GROUP", "PERFORMER", "ALBOM"])

        if enter_edit == "GROUP":
            enter_old_group = enterbox("Enter the old group name: ", "Edit")
            enter_new_group = enterbox("Enter a new group name: ", "Edit")
            for i in dict_var_read:
                count_all += 1
                if i == enter_old_group.title():
                    dict_var_read[enter_old_group.title()] = dict_var_read.pop(enter_new_group.title())
                else:
                    count += 1
            if count_all == count:
                msgbox(f"{enter_old_group.title()} group not found!")

        elif enter_edit == "PERFORMER":
            enter_user_edit = buttonbox("What you want to do specifically:", "Edit", ["REWRITE", "RENAME"])

            if enter_user_edit == "REWRITE":
                number_rewrite = enterbox("How many performers do you want to record?", "Rewrite")
                enter_group = enterbox("Enter a group name:")
                enter_new_performer = []
                if number_rewrite <= 10:
                    for i in range(number_rewrite):
                        enter_new_performer.append(enterbox("Enter the name of the artist: "))
                    for i in range(len(enter_new_performer)):
                        enter_new_performer[i] = enter_new_performer[i].title()
                    dict_var_read[enter_group.title()]["performer"] = enter_new_performer
                else:
                    msgbox("The maximum number of singers must be 10!")

            elif enter_user_edit == "RENAME":
                enter_group = enterbox("Enter a group name: ")
                enter_old_performer = enterbox("Enter the old artist name:")
                for i in dict_var_read[enter_group.title()]["performer"]:
                    if enter_old_performer == i:
                        enter_new_performer = enterbox("Enter the new artist name:")
                        dict_var_read[enter_group.title()]["performer"][i] = enter_new_performer.title()
                        break
                    else:
                        msgbox(f"{enter_old_performer.title()} performer not found!")

        elif enter_edit == "PERFORMER":
            enter_user_edit = buttonbox("What you want to do specifically:", "Edit", ["REWRITE", "RENAME"])

            if enter_user_edit == "REWRITE":
                number_rewrite = enterbox("How many alboms do you want to record?", "Rewrite")
                enter_group = enterbox("Enter a group name:")
                enter_new_albom = []
                if number_rewrite <= 10:
                    for i in range(number_rewrite):
                        enter_new_albom.append(enterbox("Enter the album name: "))
                    for i in range(len(enter_new_albom)):
                        enter_new_albom[i] = enter_new_albom[i].title()
                    dict_var_read[enter_group.title()]["albom"] = enter_new_albom
                else:
                    msgbox("Maximum number of albums can be 10!")

            elif enter_user_edit == "RENAME":
                enter_group = enterbox("Enter a group name: ")
                enter_old_albom = enterbox("Enter the old album name:")
                for i in dict_var_read[enter_group.title()]["albom"]:
                    if enter_old_albom == i:
                        enter_new_albom = enterbox("Enter a new album name:")
                        dict_var_read[enter_group.title()]["albom"][i] = enter_new_albom.title()
                        break
                    else:
                        msgbox(f"{enter_old_albom.title()} albom not found!")

        with open(path, "w") as file:
            json.dump(dict_var_read, file)
        msgbox("Data successfully updated!")

    elif interface == "IMPORT":
        all_import = []
        with open(path, "r") as file:
            dict_var_read = json.load(file)
        for i in dict_var_read:
            performer_import = []
            albom_import = []
            for j in dict_var_read[i]["performer"]:
                performer_import.append(j + '\n')
            for j in dict_var_read[i]["albom"]:
                albom_import.append(j + '\n')
            all_import.append(f"Group: {i}\n\nPerformer(s):\n\n{''.join(performer_import)}\nAlbom(s):\n\n{''.join(albom_import)}\n")
        if all_import:
            msgbox("".join(all_import))
        else:
            msgbox("The database is empty!")

    elif interface == "DEFAULT":
        with open(path, "w") as file:
            json.dump(dict_var, file)
        msgbox("Table returned to default data")

    else:
        break