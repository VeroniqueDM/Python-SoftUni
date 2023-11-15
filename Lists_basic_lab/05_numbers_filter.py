n = int(input())

even_numbers = []
odd_numbers = []
positive_numbers = []
negative_numbers = []

for i in range (1, n+1):
    number = int(input())
    if number >= 0:
        positive_numbers.append(number)
    else:
        negative_numbers.append(number)
    if number%2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

list_command = input()
if list_command == "even":
    print(even_numbers)
elif list_command == "odd":
    print(odd_numbers)
elif list_command == "positive":
    print(positive_numbers)
elif list_command == "negative":
    print(negative_numbers)