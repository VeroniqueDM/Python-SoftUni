numbers_string = input().split()
numbers_string_int = []

for numbers in numbers_string:
    numbers_string_int.append(int(numbers))

print(sorted(numbers_string_int))