class Device:
    def __init__(self, creater_name_var, year_var, price_var, color_var):
        self.creater_name = creater_name_var
        self.year = year_var
        self.price = price_var
        self.color = color_var

    def __repr__(self):
        return f""

class CoffeMachine(Device):
    def __init__(self, creater_name_var, year_var, price_var, color_var, container_var):
        Device.__init__(self, creater_name_var, year_var, price_var, color_var)
        self.container = container_var

    def __repr__(self):
        return f"Coffee Machine:\n\nCreater Name: {self.creater_name}\nYear: {self.year}\nPrice: {self.price}\n" \
               f"Color: {self.color}\nContainer: {self.container}"

class Blender(Device):
    def __init__(self, creater_name_var, year_var, price_var, color_var, rpm_var, speed_var):
        Device.__init__(self, creater_name_var, year_var, price_var, color_var)
        self.rpm = rpm_var
        self.speed = speed_var

    def __repr__(self):
        return f"Blender:\n\nCreater Name: {self.creater_name}\nYear: {self.year}\nPrice: {self.price}\nColor: " \
               f"{self.color}\nRpm: {self.rpm}\nSpeed: {self.speed}"

class MeatGrinder(Device):
    def __init__(self, creater_name_var, year_var, price_var, color_var, capacity_var):
        Device.__init__(self, creater_name_var, year_var, price_var, color_var)
        self.capacity = capacity_var

    def __repr__(self):
        return f"Meat Grinder:\n\nCreater Name: {self.creater_name}\nYear: {self.year}\nPrice: {self.price}\nColor: " \
               f"{self.color}\nCapacity: {self.capacity}"


coffee_machine = CoffeMachine("Philips", "2021", "350$", "Black", "2L")

blender_device = Blender("Bosch", "2022", "40$", "White", "11300", "12")
#
meat_grinder = MeatGrinder("Tefal", "2020", "100$", "Grey", "2KG")

print(coffee_machine)
print()
print(blender_device)
print()
print(meat_grinder)