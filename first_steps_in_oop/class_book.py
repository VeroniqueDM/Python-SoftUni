class Author:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

author_1 = Author("George", "RR Martin")
author_2 = Author('Andrzej', 'Sapkowski')
book_1 = Book("Game of Thrones", author_1, 654)
book_2 = Book("The Witcher", author_2, 939)

basket = []
basket.append(book_1)
basket.append(book_2)

print(book_1.author.last_name)