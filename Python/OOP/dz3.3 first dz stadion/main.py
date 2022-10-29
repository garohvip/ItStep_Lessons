class Stadion:
    def __init__(self, name_var, data_var, country_var, city_var, location_var):
        self.name = name_var
        self.data = data_var
        self.country = country_var
        self.city = city_var
        self.location = location_var

    def __repr__(self):
        return f"Name: {self.name}\nData: {self.data}\nCountry: {self.country}\nCity: {self.city}\nLocation:" \
               f" {self.location}"

    def edit_name(self, new_name):
        self.name = new_name

    def edit_data(self, new_data):
        self.data = new_data

    def edit_country(self, new_country):
        self.country = new_country

    def edit_city(self, new_city):
        self.city = new_city

    def edit_location(self, new_location):
        self.location = new_location


krivbass = Stadion("Gornyak", "02.05.1959", "Ukraine", "Kriviy Rih", "Station Pr. Metallurgov")

print(krivbass)