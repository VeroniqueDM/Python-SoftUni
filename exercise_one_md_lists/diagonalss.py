n = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]
primary_diagonal = []
secondary_diagonal = []
sum_primary = 0
sum_secondary = 0

for row in range(n):
    primary_num = matrix[row][row]
    secondary_num = matrix[row][n - 1 - row]
    sum_primary += primary_num
    primary_diagonal.append(primary_num)
    secondary_diagonal.append(secondary_num)
    sum_secondary += secondary_num

print(f'Primary diagonal: {", ".join(str(x) for x in primary_diagonal)}. Sum: {sum_primary}')
print(f'Secondary diagonal: {", ".join(str(x) for x in secondary_diagonal)}. Sum: {sum_secondary}')
