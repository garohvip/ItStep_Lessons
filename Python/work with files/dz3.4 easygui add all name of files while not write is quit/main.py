import os
from easygui import *
import random

path1 = os.path.join("data_base", "txtfile1.txt")

choices_random = [".txt", ".json", ".py", ".bat"]

while True:
    interface = buttonbox("Choise action: ", "Dictionary", ["START", "EXIT"])

    if interface == "START":
        with open(path1, "w", encoding="utf-8") as file:
            while True:
                name = (enterbox("Enter name file:", "Enter"))
                if name != "quit":
                    file.write(name + random.choice(choices_random) + "\n")
                else:
                    break
    else:
        break