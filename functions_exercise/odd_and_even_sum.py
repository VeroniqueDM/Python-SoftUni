# def odd_and_even_sum(string):
#     sum_even = 0
#     sum_odd = 0
#     for digit in range (0, len(string)):
#         current_digit = int(string[digit])
#         if current_digit % 2 == 0:
#             sum_even += current_digit
#         else:
#             sum_odd += current_digit
#     return f"Odd sum = {sum_odd}, Even sum = {sum_even}"
#
# number = input()
#
# print(odd_and_even_sum(number))
#






def get_even_and_odd(number):
    odd= 0
    even = 0
    for digit in number:
        if int(digit) % 2 == 0:
            even+=int(digit)
        else:
            odd += int(digit)
    return even, odd  ## returns a tuple with print()


number_as_string = input()

even_sum, odd_sum = get_even_and_odd(number_as_string)

print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
