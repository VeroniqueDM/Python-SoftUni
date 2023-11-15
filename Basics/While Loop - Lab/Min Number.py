number = input()
min_number = int(number)

while number != "Stop":
    if int(number)<int(min_number):
        min_number = int(number)
    number = input()


print(min_number)
