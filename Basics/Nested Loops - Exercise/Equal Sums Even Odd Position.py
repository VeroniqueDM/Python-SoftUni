lower_number = int(input())
bigger_number = int(input())
for number in range (lower_number, bigger_number + 1):
    number_to_string = str(number)
    sum_odd = 0
    sum_even = 0
    for index, digit in enumerate (number_to_string):
        if index % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd +=int(digit)
    if sum_even == sum_odd:
        print(number, end=" ")