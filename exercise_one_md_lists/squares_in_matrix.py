rows, columns = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]
equal_squares = 0
for row_idx in range(rows-1):
    for col_idx in range(columns - 1):
        first, second, third, fourth = [matrix[row_idx][col_idx], matrix[row_idx][col_idx+1],
                                        matrix[row_idx+1][col_idx], matrix[row_idx+1][col_idx+1]]
        if first == second == third == fourth:
            equal_squares +=1

print(equal_squares)