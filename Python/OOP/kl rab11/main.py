class Tvarina():
    def __init__(self, name, tip):
        self.name = name
        self.tip = tip

    def __repr__(self):
        return f"{self.name} {self.tip}"

class Tigr(Tvarina):
    pass

class Krokodil(Tvarina):
    def __init__(self, name, tip, kolvolap):
        super().__init__(name, tip)
        self.kolvolap = kolvolap

    def __repr__(self):
        return f"Name: {self.name} Tip: {self.tip} Kolvolap: {self.kolvolap}"

class Kenguru(Tvarina):
    def __init__(self, name1, tip1, kolvolap):
        super(Tvarina).__init__(name1, tip1)
        self.kolvolap = kolvolap

    def __repr__(self):
        return f"Name: {self.name} Tip: {self.tip} Kolvolap: {self.kolvolap}"


kenguru = Kenguru("Имя", "Тип", "4 лапы")

kroko = Krokodil("ИММЯМЯ", "ТИТИТИППП", "1 лапа")

print(kenguru)
print(kroko)