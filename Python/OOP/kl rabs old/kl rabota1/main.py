class Drib:
    def __init__(self, chis_par, znam_par):
        self.chis = chis_par
        self.znam = znam_par

    def reload(self, chis, znam):
        self.chis = chis
        self.znam = znam
        return "Успех"

    def __str__(self):
        return f"Числитель: {self.chis}\nЗнаменатель: {self.znam}\nВид в арифметике: {self.chis}/{self.znam}"

    def add(self):
        return f"{self.chis} + {self.znam} = {self.chis + self.znam}"

    def minus(self):
        return f"{self.chis} - {self.znam} = {self.chis - self.znam}"

    def prod(self):
        return f"{self.chis} * {self.znam} = {self.chis * self.znam}"

    def divis(self):
        if self.znam != 0:
            return f"{self.chis} / {self.znam} = {self.chis / self.znam}"
        else:
            return f"На ноль делить нельзя"


a = Drib(6, 2)

print(a)