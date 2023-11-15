n = int(input())
odd_set = set()
even_set = set()
for a in range(1,n+1):
    name = input()
    sum_ascii = sum([ord(x) for x in name])
    result = sum_ascii // a
    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

sum_even = sum(even_set)
sum_odd = sum(odd_set)

if sum_even == sum_odd:
    res = odd_set.union(even_set)

elif sum_odd > sum_even:
    res = odd_set.difference(even_set)
else:
    res = odd_set.symmetric_difference(even_set)

print(*res, sep=", ")