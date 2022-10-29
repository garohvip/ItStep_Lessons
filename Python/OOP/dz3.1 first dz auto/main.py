class Car:
    def __init__(self, make_var, model_var, engine_var, year_var, color_var, price_var):
        self.make = make_var
        self.model = model_var
        self.engine = engine_var
        self.year = year_var
        self.color = color_var
        self.price = price_var

    def __repr__(self):
        return f"Make: {self.make}\nModel: {self.model}\nEngine: {self.engine}\nYear: {self.year}\nColor:" \
               f" {self.color}\nPrice: {self.price}"

    def edit_make(self, new_make):
        self.make = new_make

    def edit_model(self, new_model):
        self.model = new_model

    def edit_engine(self, new_engine):
        self.engine = new_engine

    def edit_year(self, new_year):
        self.year = new_year

    def edit_color(self, new_color):
        self.color = new_color

    def edit_price(self, new_price):
        self.price = new_price


camry = Car("Toyota", "Camry", "3.6L", "2009", "Black", "10000$")

print(camry)