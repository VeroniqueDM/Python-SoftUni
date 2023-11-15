numbers = input().split()
numbers_int = []

for number in numbers:
    numbers_int.append(int(number))

def min_value(list_num):
    return min(list_num)


def max_value(list_num):
    return max(list_num)


def sum_value(list_num):
    return sum(list_num)



print(f"The minimum number is {min_value(numbers_int)}")
print(f"The maximum number is {max_value(numbers_int)}")
print(f"The sum number is: {sum_value(numbers_int)}")