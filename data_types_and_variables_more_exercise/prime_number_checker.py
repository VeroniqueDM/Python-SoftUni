number = int(input())
is_prime = True
for i in range (2, number):
    if number % i != 0:
        continue
    else:
        is_prime = False


print(is_prime)