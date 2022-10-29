import os.path
import json
from prettytable import PrettyTable


# "BMW 920", "2020", "Germany", "5.5", "red", "50000"
class Cars:
    def __init__(self, model_par, age_par, producer_par, capacity_par, color_par, price_par, win_cod_par):
        self.model = model_par
        self.age = age_par
        self.producer = producer_par
        self.capacity = capacity_par
        self.color = color_par
        self.price = price_par
        self.winCod = win_cod_par

    def __repr__(self):
        return f'{self.model}, {self.age}, {self.producer}, {self.capacity}, {self.color}, {self.price}, {self.winCod}'

    def change_model(self, new_model):
        self.model = new_model
        return "Saved"

    def change_age(self, new_age):
        self.age = new_age
        return "Saved"

    def change_producer(self, new_producer):
        self.producer = new_producer
        return "Saved"

    def change_capacity(self, new_capacity):
        self.capacity = new_capacity
        return "Saved"

    def change_color(self, new_color):
        self.color = new_color
        return "Saved"

    def change_price(self, new_price):
        self.price = new_price
        return "Saved"


class Autosalon:
    def __init__(self, file_name):
        self.file_name = file_name + ".json"
        self.path = os.path.join("", self.file_name)

    def add_car(self, new_car):
        with open(self.path, "r") as file1:
            a_car = json.load(file1)
        a_car[new_car.winCod] = {"Model": new_car.model, "Color": new_car.color, "Age": new_car.age,
                                 "Price": new_car.price, "Capacity": new_car.capacity, "Producer": new_car.producer}
        with open(self.path, "w") as file1:
            json.dump(a_car, file1)
        return f'Tour {new_car} added'

    def all_car(self):
        with open(self.path, "r") as file1:
            file = json.load(file1)
        return ''.join([f"{i}, {file.get(i).get('Model')}, {file.get(i).get('Color')}, {file.get(i).get('Age')}, "
                         f"{file.get(i).get('Price')}, {file.get(i).get('Capacity')}, {file.get(i).get('Producer')}\n" for i in file])

    def __repr__(self):
        return self.file_name

    def rem_car(self, remove_car):
        with open(self.path, "r") as file1:
            file = json.load(file1)
        file.pop(remove_car.winCod)
        with open(self.path, "w") as file1:
            json.dump(file, file1)
        return f"Your {remove_car.model} is delete from database"

    def update_car(self, update_car):
        with open(self.path, "r") as file:
            read_json = json.load(file)
        read_json[update_car.winCod] = {"Model": update_car.model, "Color": update_car.color, "Age": update_car.age,
                                        "Price": update_car.price, "Capacity": update_car.capacity,
                                        "Producer": update_car.producer}
        with open(self.path, "w") as file:
            json.dump(read_json, file)
        return f"{update_car.model} updated!"

    def compare_auto(self, auto1_vincode, auto2_vincode):
        table = PrettyTable()
        with open(self.path, "r") as file:
            read_json = json.load(file)
        # equals = []
        # no_equals = []
        table.field_names = [read_json[auto1_vincode.winCod]["Model"], "==/!=", read_json[auto2_vincode.winCod]["Model"]]
        for i in read_json[auto1_vincode.winCod]:
            if read_json[auto1_vincode.winCod][i] == read_json[auto2_vincode.winCod][i]:
                table.add_row([read_json[auto1_vincode.winCod][i], "==", read_json[auto2_vincode.winCod][i]])
        #         equals.append(f"\n{read_json[auto1_vincode.winCod]['Model']} {i} - {read_json[auto1_vincode.winCod][i]} == "
        #                       f"{read_json[auto2_vincode.winCod]['Model']} {i} - {read_json[auto2_vincode.winCod][i]}")
            else:
                table.add_row([read_json[auto1_vincode.winCod][i], "!=", read_json[auto2_vincode.winCod][i]])
        #         no_equals.append(f"\n{read_json[auto1_vincode.winCod]['Model']} {i} - {read_json[auto1_vincode.winCod][i]} != "
        #                       f"{read_json[auto2_vincode.winCod]['Model']} {i} - {read_json[auto2_vincode.winCod][i]}")
        # return f"Равные параметры:{' '.join(equals)}\n\n" \
        #        f"Неравные параметры:{' '.join(no_equals)}"
        return table


BMW920 = Cars("BMW 920", "2020", "Germany", "5.5L", "red", "50000$", "FA232312513DSGT")
Reno20 = Cars("Reno 20", "2018", "France", "5.0L", "black", "45000$", "IGH63264IKK24H2JH4")
camry = Cars("Toyota camry", "1999", "Japan", "3.6L", "green", "10000$", "GJ35J89GJ853JG9J2G")
autos = Autosalon(file_name="base")

print(autos.compare_auto(BMW920, camry))
# autosalon.add_car(Reno20)

# autosalon.rem_car(BMW920)
# print(autos.add_car(BMW920))
# print(autos.add_car(camry))
# print(autos.rem_car(BMW920))
# print(Reno20.change_capacity("5.5L"))
# print(Reno20.change_color("red"))
# print(autos.update_car(Reno20))
# print(autos.all_car())
