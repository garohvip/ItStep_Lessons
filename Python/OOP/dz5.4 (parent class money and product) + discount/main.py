class Money:
    def __init__(self, money_var, dime_var):
        self.money = money_var
        self.dime = dime_var
        self.money_dime = self.money + (self.dime / 100)

    def __repr__(self):
        return f"В кошельке: {self.money} грн и {self.dime} копеек или же {self.money_dime} грн"


class Product(Money):
    def __init__(self, money_var, dime_var):
        Money.__init__(self, money_var, dime_var)
        self.money_dime = self.money + (self.dime / 100)

    def buy(self, money_price, dime_price=0):
        money_dime_price = money_price + (dime_price / 100)
        if money_dime_price >= 100:
            money_dime_price = money_dime_price - (money_dime_price * 10 / 100)
            if (self.money_dime - money_dime_price) < 0:
                return f"В кошельке: {self.money_dime} грн\nВы заплатили {money_dime_price} грн\nУ Вас осталось " \
                       f"{self.money_dime - money_dime_price} грн. Вы в долгах перед магазином"
            if (self.money_dime - money_dime_price) >= 0:
                return f"В кошельке: {self.money_dime} грн\nВы заплатили {money_dime_price} грн\nУ Вас осталось " \
                       f"{self.money_dime - money_dime_price} грн."
        elif money_dime_price >= 500:
            money_dime_price = money_dime_price - (money_dime_price * 50 / 100)
            if (self.money_dime - money_dime_price) < 0:
                return f"В кошельке: {self.money_dime} грн\nВы заплатили {money_dime_price} грн\nУ Вас осталось " \
                       f"{self.money_dime - money_dime_price} грн. Вы в долгах перед магазином"
            if (self.money_dime - money_dime_price) >= 0:
                return f"В кошельке: {self.money_dime} грн\nВы заплатили {money_dime_price} грн\nУ Вас осталось " \
                       f"{self.money_dime - money_dime_price} грн."
        elif money_dime_price < 100:
            if (self.money_dime - money_dime_price) < 0:
                return f"В кошельке: {self.money_dime} грн\nВы заплатили {money_dime_price} грн\nУ Вас осталось " \
                       f"{self.money_dime - money_dime_price} грн. Вы в долгах перед магазином"
            if (self.money_dime - money_dime_price) >= 0:
                return f"В кошельке: {self.money_dime} грн\nВы заплатили {money_dime_price} грн\nУ Вас осталось " \
                       f"{self.money_dime - money_dime_price} грн."


groshi = Money(100, 50)
print(groshi)
print()
magaz = Product(1500, 50)
print(magaz.buy(630, 50))