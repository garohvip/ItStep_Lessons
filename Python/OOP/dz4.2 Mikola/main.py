class Mikola:
    def __init__(self, name_var, age_var):
        self.name = name_var
        self.age = age_var

    def __repr__(self):
        if self.name != "Коля":
            return f"Я не {self.name}, а Коля и мне {self.age} лет."
        else:
            return f"Я {self.name} и мне {self.age} лет."


random_name = Mikola("Коля", "43")

print(random_name)