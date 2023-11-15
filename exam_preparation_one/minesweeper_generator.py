def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


def neighbour_cells(row, col, matrix):
    result = 0
    if is_valid(row-1,col, len(matrix)):
        if matrix[row-1][col] == "*":
            result += 1
    if is_valid(row+1,col, len(matrix)):
        if matrix[row+1][col] == "*":
            result += 1
    if is_valid(row,col+1, len(matrix)):
        if matrix[row][col+1] == "*":
            result += 1
    if is_valid(row,col-1, len(matrix)):
        if matrix[row][col-1] == "*":
            result += 1
    if is_valid(row-1,col-1, len(matrix)):
        if matrix[row-1][col-1] == "*":
            result += 1
    if is_valid(row-1,col+1, len(matrix)):
        if matrix[row-1][col+1] == "*":
            result += 1
    if is_valid(row+1,col-1, len(matrix)):
        if matrix[row+1][col-1] == "*":
            result += 1
    if is_valid(row+1,col+1, len(matrix)):
        if matrix[row+1][col+1] == "*":
            result += 1
    return result


size = int(input())
matrix = [[0 for x in range(size)] for _ in range(size)]
count_bombs = int(input())
bomb_coords = []
for _ in range(count_bombs):
    bomb_coords.append(eval(input()))

for coords in bomb_coords:
    row, col = coords[0],coords[1]
    matrix[row][col] = "*"

for r in range(size):
    for c in  range(size):
        value = neighbour_cells(r,c,matrix)
        if matrix[r][c] != "*":
            matrix[r][c] = value


for rows in matrix:
    print(*rows, sep=" ")
