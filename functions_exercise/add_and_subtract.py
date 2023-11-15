def sum_numbers(a, b):
    return a+b


def subtract(c, d):
    return c - d


def add_and_subract():
    number_one = int(input())
    number_two = int(input())
    number_three = int(input())
    x = sum_numbers(number_one, number_two)
    y = subtract(x, number_three)
    print(y)

add_and_subract()