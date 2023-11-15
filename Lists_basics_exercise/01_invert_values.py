string_of_numbers = input().split(" ")
opposite_numbers = []
for index in range(len(string_of_numbers)):
    opposite_number = -int(string_of_numbers[index])
    opposite_numbers.append(opposite_number)

print(opposite_numbers)