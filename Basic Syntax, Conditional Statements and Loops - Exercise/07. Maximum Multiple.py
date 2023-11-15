divisor = int (input())
boundary = int (input())

for number in range (0, boundary+1):
    if number%divisor == 0:
        largest_number = number

print(largest_number)
