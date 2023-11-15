fav_book = input()
current_book = input()
count_books = 0
while current_book != "No More Books":

    if current_book == fav_book:
        print(f"You checked {count_books} books and found it.")
        break
    count_books = count_books + 1
    current_book = input()

if current_book == "No More Books":
    print("The book you search is not here!")
    print(f"You checked {count_books} books.")