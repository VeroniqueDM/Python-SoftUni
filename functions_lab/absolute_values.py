numbers_list = input().split()


for numbers in range (0, len(numbers_list)):
    numbers_list[numbers] = abs(float(numbers_list[numbers]))

print(numbers_list)