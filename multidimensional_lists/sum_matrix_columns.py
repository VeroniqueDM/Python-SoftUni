rows, columns = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split()] for y in range(rows)]
sums = [sum(matrix[i][:len(matrix[i])]) for i in range(len(matrix))]

for i in range(columns):
    col_sum = 0
    for j in range(rows):
        col_sum += matrix[j][i]
    print(col_sum)
