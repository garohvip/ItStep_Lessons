class Car:

    wheels_number = 4

    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed


mazda_car = Car(name="Mazda CX7", color="Red", year=2017, is_crashed=True)

print(mazda_car.name)
print(mazda_car.year)
print(mazda_car.color)
if mazda_car.is_crashed:
    print(mazda_car.name, "Бита шо пиздец")
else:
    print(mazda_car.name, "Прям сосочка тачечка")
print(mazda_car.wheels_number)

number_of_wheels_of_3_cars = Car.wheels_number * 3
print(number_of_wheels_of_3_cars)