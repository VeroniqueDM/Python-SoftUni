first_number = input()
largest_number = ""
for index in range (9, -1, -1):
    for char in first_number:
        if char == str(index):
            largest_number += str(char)
print(largest_number)