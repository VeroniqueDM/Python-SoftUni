number = int(input())

def perfect_number(a_number):
    proper_positive_divisors_list = []
    for i in range (1, a_number + 1):
        if a_number % i == 0:
            proper_positive_divisors_list.append(i)
    if sum(proper_positive_divisors_list) / 2 == a_number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


print(perfect_number(number))

