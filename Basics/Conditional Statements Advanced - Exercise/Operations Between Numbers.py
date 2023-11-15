number_one = int(input())
number_two = int(input())
operator = input()
result = 0
odd_even = 0


if operator == "+" or operator == "*" or operator == "-":
    if operator == "+":
        result = number_one + number_two
    elif operator == "-":
        result = number_one - number_two
    elif operator == "*":
        result = number_one * number_two
    if result % 2 == 0:
        odd_even = "even"
    else:
        odd_even = "odd"
    print(f"{number_one} {operator} {number_two} = {result} - {odd_even}")
elif (operator == "/" or operator == "%") and number_two == 0:
    print(f"Cannot divide {number_one} by zero")
elif operator == "/":
    result = number_one / number_two
    print(f"{number_one} / {number_two} = {result:.2f}")
elif operator == "%":
    result = number_one % number_two
    print(f"{number_one} % {number_two} = {result}")
