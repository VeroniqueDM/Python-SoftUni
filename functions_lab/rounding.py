numbers_list = input().split()


def rounded_list():
    for numbers in range (0, len(numbers_list)):
        numbers_list[numbers] = round(float(numbers_list[numbers]))

    return numbers_list


print(rounded_list())