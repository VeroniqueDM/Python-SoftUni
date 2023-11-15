


def factorial_division(a,b):
    factorial_a = 1
    factorial_b = 1
    for num in range (1, a +1):
        factorial_a *= num
    for num_two in range (1, b +1):
        factorial_b *= num_two
    result = factorial_a / factorial_b
    return result



number_one = int(input())
number_two = int(input())

print(f"{factorial_division(number_one,number_two):.2f}")