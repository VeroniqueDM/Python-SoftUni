command = input()
sum_prime = 0
sum_non_prime = 0
while command != "stop":
    number = int(command)
    if number < 0:
        print("Number is negative.")
        command = input()
        continue
    denominator_count = 0
    for i in range(2, number + 1):
        if number % i == 0:
            denominator_count += 1

    if denominator_count == 1:
        sum_prime += number
    elif denominator_count > 1:
        sum_non_prime += number

    command = input()
print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
