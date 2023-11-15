def is_inside(row, col):
    return 0 <= row < 5 and 0 <= col < 5


def next_position(row, col, command):
    step = int(command[2])
    if command[1] == "left":
        new_col = col - step
        return row, new_col

    elif command[1] == "right":
        new_col = col + step
        return row, new_col
    elif command[1] == "up":
        new_row = row - step

        return new_row, col
    elif command[1] == "down":
        new_row = row + step

        return new_row, col


def hit_position(row, col, command, matrix):
    if command[1] == "left":
        for ind in range(col, -1, -1):
            if matrix[row][ind] == "x":
                return row, ind
        else:
            return None, None
    elif command[1] == "right":
        for ind in range(col, 5):
            if matrix[row][ind] == "x":
                return row, ind

        else:
            return None, None
    elif command[1] == "down":
        for ind in range(row, 5):
            if matrix[ind][col] == "x":
                return ind, col
        else:
            return None, None
    elif command[1] == "up":
        for ind in range(row, -1, -1):
            if matrix[ind][col] == "x":
                return ind, col
        else:
            return None, None


matrix = [[x for x in input().split()] for _ in range(5)]

num_commands = int(input())
row_position = 0
col_position = 0
targets_counter = 0
for r in range(5):
    for c in range(5):
        if matrix[r][c] == "A":
            row_position = r
            col_position = c
        elif matrix[r][c] == "x":
            targets_counter += 1

current_row = row_position
current_col = col_position
hit_targets_coorr = []
hit_targets = 0
for a in range(num_commands):
    command = input().split()
    if command[0] == "move":

        new_row, new_col = next_position(current_row, current_col, command)
        if is_inside(new_row,new_col) and matrix[new_row][new_col] != "x":
            current_row, current_col = new_row, new_col
    else:
        hit_row, hit_col = hit_position(current_row, current_col, command, matrix)
        if hit_col != None and hit_row != None:
            matrix[hit_row][hit_col] = "."
            targets_counter -= 1
            hit_targets += 1
            hit_targets_coorr.append([hit_row, hit_col])
    if targets_counter == 0:
        break

if targets_counter == 0:
    print(f"Training completed! All {hit_targets} targets hit.")
else:
    print(f"Training not completed! {targets_counter} targets left.")
if hit_targets_coorr:
    for a in hit_targets_coorr:
        print(a)
