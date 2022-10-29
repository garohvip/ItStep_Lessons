class Car:
    def __init__(self, name_var, year_var, publisher_var, genre_var, autor_var, price_var):
        self.name = name_var
        self.year = year_var
        self.publisher = publisher_var
        self.genre = genre_var
        self.autor = autor_var
        self.price = price_var

    def __repr__(self):
        return f"Name: {self.name}\nYear: {self.year}\nPublisher: {self.publisher}\nGenre: {self.genre}\nAutor:" \
               f" {self.autor}\nPrice: {self.price}"

    def edit_name(self, new_name):
        self.name = new_name

    def edit_year(self, new_year):
        self.year = new_year

    def edit_publisher(self, new_publisher):
        self.publisher = new_publisher

    def edit_genre(self, new_genre):
        self.genre = new_genre

    def edit_autor(self, new_autor):
        self.autor = new_autor

    def edit_price(self, new_price):
        self.price = new_price


book = Car("Harry Potter", "2001", "Ukraine", "Criminal", "Ron Weasleyi", "1500$")

print(book)