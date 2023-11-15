def calc_fact(number):
    if number == 0:
        return 1
    return number * calc_fact(number - 1)


num = int(input())

print(calc_fact(num))
