import os.path

class Cars:
    def __init__(self, model_par, age_par, producer_par, capacity_par, color_par, price_par):
        self.model = model_par
        self.age = age_par
        self.producer = producer_par
        self.capacity = capacity_par
        self.color = color_par
        self.price = price_par

    def __repr__(self):
        return f'{self.model}, {self.age}, {self.producer}, {self.capacity}, {self.color}, {self.price}'

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


class Car_showroom:
    # 1
    # def __init__(self):
    #     self.cars = []
    #
    # def __repr__(self):
    #     return f'{self.cars}'
    # def __repr__(self):
    #     str_reviews = ""
    #     for ind in range(1, len(self.cars) + 1):
    #         str_reviews = str_reviews + f'Rewiews {ind}: {self.cars[ind - 1]}\n'
    # 2
    def __init__(self, file_name):
        self.file_name = file_name + ".txt"
        self.path = os.path.join("", self.file_name)

    def add_car(self, new_car):
        file = open(self.path, "a")
        file.write(str(new_car) + "\n")
        file.close()

    def __repr__(self):
        file = open(self.path, "r")
        return f"{' '.join([line for line in file])}"

    def rem_car(self, remove_car):
        file = open(self.path, "r")
        line_list = [line for line in file if not str(remove_car) in line]
        file.close()
        file = open(self.path, "w")
        file.write("".join(line_list))
        file.close()


BMW920 = Cars("BMW 920", "2020", "Germany", "5.5", "red", "50000")
Reno20 = Cars("Reno 20", "2018", "France", "5.0", "black", "45000")
autosalon = Car_showroom(file_name="avtoslon")
# autosalon.add_car(BMW920)
# autosalon.add_car(Reno20)

autosalon.rem_car(BMW920)
print(autosalon)