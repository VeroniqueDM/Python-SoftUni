number = input()
max_number = int(number)

while number != "Stop":
    if int(number)>int(max_number):
        max_number = int(number)
    number = input()


print(max_number)
