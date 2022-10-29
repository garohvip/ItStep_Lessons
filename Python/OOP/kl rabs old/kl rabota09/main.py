class Books:

    def __init__(self, name_par, age_par, publisher_par, genre_par, author_par, price_par):
        self.name = name_par
        self.age = age_par
        self.publisher = publisher_par
        self.genre = genre_par
        self.author = author_par
        self.price = price_par
        self.review_list = []

    def __str__(self):
        str_reviews = "\n"
        return f"{self.name}, {self.age}, {self.publisher}, {self.genre}, {self.author}, {self.price}\n" \
               f"""{"".join([str_reviews + f'Reviews {i}: {self.review_list[i-1]}' for i in range(1, len(self.review_list)+1)])}"""

    def change_name(self, new_name):
        self.name = new_name
        return "Saved"

    def change_age(self, new_age):
        self.age = new_age
        return "Saved"

    def change_producer(self, new_publisher):
        self.publisher = new_publisher
        return "Saved"

    def change_genre(self, new_genre):
        self.genre = new_genre
        return "Saved"

    def change_author(self, new_author):
        self.author = new_author
        return "Saved"

    def change_price(self, new_price):
        self.price = new_price
        return "Saved"

    def add_review(self, new_review):
        return self.review_list.append(new_review)


class BookReview:

    def __init__(self, review_par):
        self.review = review_par

    def __repr__(self):
        return self.review


metro2033 = Books("Метро 2033", "2020", "Навчальна книга - Богдан", "Фантастика", "Дмитро Ґлуховський", "449.00")
review_user1 = BookReview("aaaaaaaaaaaaaaa")
review_user2 = BookReview("bbbbbbbbbbbbbbb")
review_user3 = BookReview("ccccccccccccccc")
print(metro2033)
metro2033.add_review(review_user1)
metro2033.add_review(review_user2)
metro2033.add_review(review_user3)
print(metro2033)