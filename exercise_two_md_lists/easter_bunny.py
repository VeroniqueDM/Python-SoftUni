def is_valid (row,col, size):
    return 0<=row<size and 0<=col<size


def move_up(row,col):
    return  row -1, col


def move_down(row,col):
    return row+1, col


def move_right(row,col):
    return row, col +1

def move_left(row,col):
    return row, col-1

size = int(input())

matrix = []
bunny_row = 0   
bunny_col = 0

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)
    for col in range(size):
         if matrix[row][col] == "B":
             bunny_row = row
             bunny_col = col




directions = {"right":move_right, "left":move_left, "up":move_up, "down":move_down}
best_score = float('-inf')
best_dir = ""
best_path = []
for direction,step in directions.items():
    current_row, current_col = bunny_row,bunny_col
    current_score = 0
    path = []
    while True:
        current_row,current_col = step(current_row, current_col)
        if not is_valid(current_row,current_col,size):
            break
        if matrix[current_row][current_col] == "X":
            break
        path.append([current_row, current_col])

        current_score += int(matrix[current_row][current_col])


    if current_score > best_score:
        best_score = current_score
        best_dir = direction
        best_path = path


print(best_dir)
for step in best_path:
    print(step)
print(best_score)