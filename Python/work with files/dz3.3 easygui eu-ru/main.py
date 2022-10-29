import os
from easygui import *

path = os.path.join("data_base", "en-ua.txt")

while True:
    interface = buttonbox("Choise action: ", "Dictionary", ["ADD", "DEL", "EXAM", "SEARCH", "EXIT"])

    if interface == "ADD":
        words = multenterbox("Enter your words: ", "Dictionary", ["En", "Ru"])
        file = open(path, "a", encoding="utf-8")
        # file.write(f'{words[0]} {words[1]}\n')
        file.write(" ".join(words) + "\n")
        file.close()

    elif interface == "SEARCH":
        word = enterbox("Enter your word")
        with open(path, "r", encoding="utf-8") as file:
            for i in file:
                if i.startswith(word + " ") or i.endswith(word + "\n"):
                    msgbox(i.replace(word, ""))
    elif interface == "DEL":
        word = enterbox("Enter you word")
        with open(path, "r", encoding="utf-8") as file:
            list_line = [i for i in file if i.startswith(word + " ") == False and i.endswith(word + "\n") == False]
        with open(path, "w", encoding="utf-8") as file:
            file.write("".join(list_line))
    elif interface == "EXAM":
        with open(path, "r", encoding="utf-8") as file:
            rate = 0
            read_file = file.readlines()
            enter_user = buttonbox("Экзамен: RU or EU", "Examen", ["RU", "EU"])
            if enter_user == "RU":
                for i in read_file:
                    words = i.split()
                    quest = enterbox(f"This? {words[1]}")
                    if quest == i.split()[0]:
                        rate += 1
            elif enter_user == "EU":
                for i in read_file:
                    words = i.split()
                    quest = enterbox(f"This? {words[0]}")
                    if quest == i.split()[1]:
                        rate += 1
        msgbox(f'you quessed {rate} words out of {len(read_file)}')
    else:
        break