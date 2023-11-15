numbers_list = input().split()
numbers_list_as_digits = []
for numbers in numbers_list:
    numbers_list_as_digits.append(int(numbers))

is_even_lambda = lambda x: x%2 == 0

# def is_even(string):
#
#     for elements in string:
#         current_number = int(string[elements])
#         if current_number % 2 == 0:
#             return True



even_numbers = list(filter(is_even_lambda, numbers_list_as_digits))


print(even_numbers)