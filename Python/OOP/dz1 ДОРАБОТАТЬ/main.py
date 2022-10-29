import json
from easygui import *
import os.path


class Car:

    def __init__(self, car_name, path_in_class):
        with open(path_in_class, "r") as file_in_class:
            json_read_class = json.load(file_in_class)
        self.car_name = car_name
        self.make = json_read_class.get(car_name).get("make")
        self.model = json_read_class.get(car_name).get("model")
        self.year = json_read_class.get(car_name).get("year")
        self.engine = json_read_class.get(car_name).get("engine")
        self.color = json_read_class.get(car_name).get("color")
        self.price = json_read_class.get(car_name).get("price")

    def __str__(self):
        return f"Make and model: {self.make} {self.model}\nYear: {self.year}\nEngine: {self.engine}L\nColor: {self.color}\nPrice: {self.price}$\n\n"

    def add(self, make, model, year, engine, color, price):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine
        self.color = color
        self.price = price

    def edit_all(self, make, model, year, engine, color, price):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine
        self.color = color
        self.price = price

    def edit_make(self, make):
        self.make = make

    def edit_model(self, model):
        self.model = model

    def edit_year(self, year):
        self.year = year

    def edit_engine(self, engine):
        self.engine = engine

    def edit_color(self, color):
        self.color = color

    def edit_price(self, price):
        self.price = price


path = os.path.join("base.json")
car12 = Car("car1", path)
# car2 = Car("Toyota", "Camry", "2020", "2", "Black", "29000")
# car3 = Car("Audi", "RS6", "2021", "4", "Green", "130000")
# cars = {"car1": ["Volkswagen", "Polo", "2016", "1.4", "White", "10000"]}

while True:

    interface = buttonbox("Choose button:", "Cars", ["ADD INFO", "OUTPUT INFO", "EDIT INFO", "EXIT"])

    if interface == "ADD INFO":
        with open(path, "r") as file:
            json_read = json.load(file)
        keys = json_read.keys()
        var_new_car = []
        while True:
            add_key = enterbox("Enter key for dict: (Пример: car1, car2, ...) (Кнопку Cancel НЕ НАЖИМАТЬ!"
                               "ее не должно существовать)", "Enter key")
            if add_key in keys:
                msgbox("This key already exists. Write a new one.")
                continue
            elif add_key == "":
                msgbox("Do not leave the field blank. Write a new one.")
                continue
            else:
                var_new_car = multenterbox("Enter car data:", "Enter data", ["MAKE:", "MODEL:", "YEAR:", "ENGINE:",
                                                                             "COLOR", "PRICE"])
                break
        json_read.update({add_key: {"make": var_new_car[0], "model": var_new_car[1], "year": var_new_car[2], "engine": var_new_car[3], "color": var_new_car[4], "price": var_new_car[5]}})
        with open(path, "w") as file:
            json.dump(json_read, file)


    elif interface == "OUTPUT INFO":

        interface_output = buttonbox("Select the car you want to withdraw:", "Output", ["ALL"])

        if interface_output == "ALL":
            print(car12)


    # elif interface == "EDIT INFO":
    #
    #     interface_edit = buttonbox("What you want to change:", "Edit", ["MAKE", "MODEL", "YEAR", "ENGINE", "COLOR", "PRICE", "ALL"])
    #
    #     if interface_edit == "MAKE":
    #
    #         choose_car = buttonbox("Choose car that want to change:", "Cars", ["CAR1", "CAR2", "CAR3"])
    #
    #         if choose_car == "CAR1":
    #             car1.edit_make(enterbox("Enter new make car:", "Enter new info"))
    #
    #         elif choose_car == "CAR2":
    #             car2.edit_make(enterbox("Enter new make car:", "Enter new info"))
    #
    #         elif choose_car == "CAR3":
    #             car3.edit_make(enterbox("Enter new make car:", "Enter new info"))
    #
    #         msgbox("Successfully updated!")
    #
    #     elif interface_edit == "MODEL":
    #
    #         choose_car = buttonbox("Choose car that want to change:", "Cars", ["CAR1", "CAR2", "CAR3"])
    #
    #         if choose_car == "CAR1":
    #             car1.edit_model(enterbox("Enter new model car:", "Enter new info"))
    #
    #         elif choose_car == "CAR2":
    #             car2.edit_model(enterbox("Enter new model car:", "Enter new info"))
    #
    #         elif choose_car == "CAR3":
    #             car3.edit_model(enterbox("Enter new model car:", "Enter new info"))
    #
    #         msgbox("Successfully updated!")
    #
    #     elif interface_edit == "YEAR":
    #
    #         choose_car = buttonbox("Choose car that want to change:", "Cars", ["CAR1", "CAR2", "CAR3"])
    #
    #         if choose_car == "CAR1":
    #             car1.edit_year(enterbox("Enter new year car:", "Enter new info"))
    #
    #         elif choose_car == "CAR2":
    #             car2.edit_year(enterbox("Enter new year car:", "Enter new info"))
    #
    #         elif choose_car == "CAR3":
    #             car3.edit_year(enterbox("Enter new year car:", "Enter new info"))
    #
    #         msgbox("Successfully updated!")
    #
    #     elif interface_edit == "ENGINE":
    #
    #         choose_car = buttonbox("Choose car that want to change:", "Cars", ["CAR1", "CAR2", "CAR3"])
    #
    #         if choose_car == "CAR1":
    #             car1.edit_engine(enterbox("Enter new engine car:", "Enter new info"))
    #
    #         elif choose_car == "CAR2":
    #             car2.edit_engine(enterbox("Enter new engine car:", "Enter new info"))
    #
    #         elif choose_car == "CAR3":
    #             car3.edit_engine(enterbox("Enter new engine car:", "Enter new info"))
    #
    #         msgbox("Successfully updated!")
    #
    #     elif interface_edit == "COLOR":
    #
    #         choose_car = buttonbox("Choose car that want to change:", "Cars", ["CAR1", "CAR2", "CAR3"])
    #
    #         if choose_car == "CAR1":
    #             car1.edit_color(enterbox("Enter new color car:", "Enter new info"))
    #
    #         elif choose_car == "CAR2":
    #             car2.edit_color(enterbox("Enter new color car:", "Enter new info"))
    #
    #         elif choose_car == "CAR3":
    #             car3.edit_color(enterbox("Enter new color car:", "Enter new info"))
    #
    #         msgbox("Successfully updated!")
    #
    #     elif interface_edit == "PRICE":
    #
    #         choose_car = buttonbox("Choose car that want to change:", "Cars", ["CAR1", "CAR2", "CAR3"])
    #
    #         if choose_car == "CAR1":
    #             car1.edit_price(enterbox("Enter new price car:", "Enter new info"))
    #
    #         elif choose_car == "CAR2":
    #             car2.edit_price(enterbox("Enter new price car:", "Enter new info"))
    #
    #         elif choose_car == "CAR3":
    #             car3.edit_price(enterbox("Enter new price car:", "Enter new info"))
    #
    #         msgbox("Successfully updated!")
    #
    #     elif interface_edit == "ALL":
    #
    #         choose_car = buttonbox("Choose car that want to change:", "Cars", ["CAR1", "CAR2", "CAR3"])
    #
    #         if choose_car == "CAR1":
    #             car1.edit_all(multenterbox("Enter new make car:", "Enter new info", ["Make:", "Model:", "Year:", "Engine:", "Color:", "Price:"]))
    #
    #         elif choose_car == "CAR2":
    #             car2.edit_all(multenterbox("Enter new make car:", "Enter new info", ["Make:", "Model:", "Year:", "Engine:", "Color:", "Price:"]))
    #
    #         elif choose_car == "CAR3":
    #             car3.edit_all(multenterbox("Enter new make car:", "Enter new info", ["Make:", "Model:", "Year:", "Engine:", "Color:", "Price:"]))
    #
    #         msgbox("Successfully updated!")

    else:
        break