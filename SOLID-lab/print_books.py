class Book:
    def __init__(self, title, author, content: str):
        self.title = title
        self.content = content
        self.author = author



class Formatter:
    def format(self, book: Book) -> str:
        return book.content

class PrePrintFlyer:
    def format(self, book:Book):
        return f"----------\n{book.title}\n----------\n{book.author}\n----------\n"

class Printer:
    def __init__(self, formatter): # <-injection. if there was a variable formatter = Formatter() in the
                                    # get_book method this would have been a violation of the dependency injection logic
        self.formatter = formatter

    def get_book(self, book: Book):
        return self.formatter.format(book)
normal_formatter = Formatter()
flyer_formatter = PrePrintFlyer()

b = Book("Title", "Author", "Content")
p = Printer(normal_formatter)
p2 = Printer(flyer_formatter)
print(p.get_book(b))
print()
print(p2.get_book(b))