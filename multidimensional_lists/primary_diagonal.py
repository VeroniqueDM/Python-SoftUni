n = int(input())
matrix = [[int(x) for x in input().split()] for y in range(n)]

sum_primary_diagonal = 0

for a in range(n):
    sum_primary_diagonal += matrix[a][a]


print(sum_primary_diagonal)