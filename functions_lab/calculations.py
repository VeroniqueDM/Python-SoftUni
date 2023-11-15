operator = input()
first_number = int(input())
second_number = int(input())

def calculation():
    if operator == "multiply":
        result = first_number * second_number
    elif operator == "divide":
        result = first_number / second_number
    elif operator == "add":
        result = first_number + second_number
    elif operator == "subtract":
        result = first_number - second_number
    result = int(result)
    return result


print(calculation())