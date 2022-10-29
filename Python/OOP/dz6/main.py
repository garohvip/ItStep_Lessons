from easygui import *
import os.path


class Client:
    def __init__(self, money_var, dime_var):
        self.money = money_var
        self.dime = dime_var
        self.money_dime = self.money + (self.dime / 100)

    def __repr__(self):
        return f"В кошельке: {self.money} грн и {self.dime} копеек или же {self.money_dime} грн"


class Magazine(Client):
    def __init__(self, money_dime, cost_var):
        super().__init__(self, money_dime)
        self.cost = cost_var

    def __repr__(self):
        # return f"В кошельке: {self.money} грн и {self.dime} копеек\nCost: {self.cost}"
        return f"{self.money_dime}, {self.cost}"

    # def buy_products(self, ):


# egdemo()
a1 = Client(50, 30)
print(a1)
# print(Magazine(a1, 25))