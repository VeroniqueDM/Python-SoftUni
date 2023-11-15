def isprime(num):
    if num==2 or num==3:
        return True
    if num%2==0 or num<2:
        return False
    for n in range(3,int(num**0.5)+1,2):
        if num%n==0:
            return False
    return True

def get_primes(num_list):

    for num in num_list:
        if isprime(num):
            yield num
        else:
            pass


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
