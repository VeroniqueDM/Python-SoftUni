def is_inside(rows, cols, size):
    return 0 <= rows < size and 0 <= cols < size

def get_neighbours(roww, col, matrix):
    size = len(matrix)
    neighbours = []
    if is_inside(roww -1, col,size) and matrix[roww-1][col] >0:
        neighbours.append([row-1, col])
    if is_inside(roww -1, col-1,size) and matrix[roww-1][col-1] >0:
        neighbours.append([row-1, col-1])
    if is_inside(roww -1, col+1,size) and matrix[roww-1][col+1] >0:
        neighbours.append([row-1, col+1])
    if is_inside(roww, col-1,size) and matrix[roww][col-1] >0:
        neighbours.append([roww, col-1])
    if is_inside(roww, col+1,size) and matrix[roww][col+1] >0:
        neighbours.append([row, col+1])
    if is_inside(roww +1, col-1,size) and matrix[roww+1][col-1] >0:
        neighbours.append([row+1, col-1])
    if is_inside(roww +1, col,size) and matrix[roww+1][col] >0:
        neighbours.append([row+1, col])
    if is_inside(roww +1, col+1,size) and matrix[roww+1][col+1] >0:
        neighbours.append([roww +1, col+1])

    return neighbours

size_matrix = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size_matrix)]

bombs = input().split()

for bomb in bombs:
    row, column =[int(x) for x in bomb.split(",")]
    if matrix[row][column]<=0:
        continue
    bomb_power = matrix[row][column]
    matrix[row][column] = 0
    neighbours = get_neighbours(row,column,matrix)
    for r, c in neighbours:
        matrix[r][c] -=bomb_power
alive_cells = []

for row in matrix:
    for item in row:
        if item > 0:
            alive_cells.append(item)
print(f'Alive cells: {len(alive_cells)}')
print(f'Sum: {sum(alive_cells)}')
for row in matrix:
    print(*row, sep=" ")

