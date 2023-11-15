rows, columns = [int(x) for x in input().split(", ")]
matrix = []
for row in range (0, rows):
    matrix.append([int(x) for x in input().split(", ")])

sum_t = 0
for r in range(len(matrix)):
    for c in matrix[r]:
        sum_t += c
print(sum_t)
print(matrix)