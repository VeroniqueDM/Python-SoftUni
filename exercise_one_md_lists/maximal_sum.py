rows, columns = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]
max_sum = -9999999999999999999
matrix_max_sum = []
for row in range(rows-2):
    for col in range(columns - 2):
        current_square = [[matrix[row][col], matrix[row][col+1], matrix[row][col+2]],
                          [matrix[row+1][col], matrix[row+1][col+1], matrix[row+1][col+2]],
                          [matrix[row+2][col], matrix[row+2][col+1], matrix[row+2][col+2]]]
        current_square_sum = sum(current_square[0]) + sum(current_square[1]) + sum(current_square[2])
        if current_square_sum > max_sum:
            max_sum = current_square_sum
            matrix_max_sum = current_square.copy()
print(f"Sum = {max_sum}")
for a in range(3):
    print(" ".join(str(x) for x in matrix_max_sum[a]))



