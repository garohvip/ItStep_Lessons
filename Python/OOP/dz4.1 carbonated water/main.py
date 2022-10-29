class Soda:
    def __init__(self, additive_var):
        self.additive = additive_var

    def __repr__(self):
        if self.additive == "":
            return f"Газированная вода"
        else:
            return f"Газированная вода с добавкой {self.additive}а"


limon = Soda("лимон")

print(limon)