command = input()
coffee_counter = 0
while command != "END":
    if command.isupper():
        if command == "CODING" or command == "CAT" or command == "DOG" or command == "MOVIE" :
            coffee_counter += 2
    else:
        if command == "coding" or command == "cat" or command == "dog" or command == "movie":
            coffee_counter += 1
    command = input()

if coffee_counter > 5 :
    print("You need extra sleep")
else:
    print(coffee_counter)