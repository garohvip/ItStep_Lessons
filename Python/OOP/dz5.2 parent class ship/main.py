class Ship:
    def __init__(self, name_var, capacity_var, cruising_range_var, year_var):
        self.name = name_var
        self.capacity = capacity_var
        self.cruising_range = cruising_range_var
        self.year = year_var

    def __repr__(self):
        return f""


class Frigate(Ship):
    def __init__(self, name_var, capacity_var, cruising_range_var, year_var, speed_var):
        Ship.__init__(self, name_var, capacity_var, cruising_range_var, year_var)
        self.speed = speed_var

    def __repr__(self):
        return f"Frigate:\n\nName: {self.name}\nCapacity: {self.capacity}\nCruising range: {self.cruising_range}\n" \
               f"Year: {self.year}\nSpeed: {self.speed}"

    def speed_var(self):
        return f"{self.speed}"


class Destroyer(Ship):
    def __init__(self, name_var, capacity_var, cruising_range_var, year_var, lens_var):
        Ship.__init__(self, name_var, capacity_var, cruising_range_var, year_var)
        self.lens = lens_var

    def __repr__(self):
        return f"Destroyer:\n\nName: {self.name}\nCapacity: {self.capacity}\nCruising range: {self.cruising_range}\n" \
               f"Year: {self.year}\nLen: {self.lens}"

    def lens_var(self):
        return f"{self.lens}"


class Cruiser(Ship):
    def __init__(self, name_var, capacity_var, cruising_range_var, year_var, lens_var, speed_var, classes_var):
        Ship.__init__(self, name_var, capacity_var, cruising_range_var, year_var)
        self.lens = lens_var
        self.speed = speed_var
        self.classes = classes_var

    def __repr__(self):
        return f"Cruiser:\n\nName: {self.name}\nCapacity: {self.capacity}\nCruising range: {self.cruising_range}\n" \
               f"Year: {self.year}\nLen: {self.lens}\nSpeed: {self.speed}\nClass: {self.classes}"


frigate_ship = Frigate("Power Ranger", "20 peoples", "300 KM", "2019", "100 KM/H")

destroyer_ship = Destroyer("Big Man", "50 peoples", "400 KM", "2005", "150 metr")

cruiser_ship = Cruiser("Hard Skill", "200 peoples", "700 KM", "1997", "200 metr", "35 KM/H", "Middle")

print(frigate_ship)
print()
print(destroyer_ship)
print()
print(cruiser_ship)