import os
from easygui import *
import random

path1 = os.path.join("data_base", "txtfile1.txt")

choices_random = [".txt", ".json", ".py", ".bat"]

while True:
    interface = buttonbox("Choise action: ", "Dictionary", ["START", "EXIT"])
    all_symobls = []
    all_symobls_end = []
    count = 0
    if interface == "START":
        with open(path1, "w", encoding="utf-8") as file:
            while True:
                name = (enterbox("Enter name file:", "Enter"))
                if name != "quit":
                    # file.write(name + random.choice(choices_random) + "\n")
                    file.write(name + "\n")
                else:
                    break
        with open(path1, "r", encoding="utf-8") as file:
            file_read = file.read().split()
        for i in file_read:
            for j in i:
                all_symobls.append(j)
        for i in range(len(all_symobls)):
            for j in all_symobls[i+1:]:
                if all_symobls[i] != j:
                    continue
                else:
                    all_symobls_end.append(all_symobls[i])

        print(all_symobls_end)
        # for k in range(len(all_symobls)):
        #     for o in range(len(all_symobls)):
        #         if all_symobls[k] == all_symobls[o]:
        #             all_symobls_end.append(k)
        # for q in all_symobls_end:
        # with open(path1, "a", encoding="utf-8") as file:
        #     file.write(f"Символы которые совпали это: {all_symobls_end}")
    else:
        break