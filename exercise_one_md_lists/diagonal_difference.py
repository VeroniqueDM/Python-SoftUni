size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]

prim_sum = 0
sec_sum = 0

for idx in range(size):
    prim_sum += matrix[idx][idx]
    sec_sum += matrix[idx][size - 1 - idx]

res = abs(prim_sum - sec_sum)
print(res)