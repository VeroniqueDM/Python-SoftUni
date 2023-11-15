def is_inside(row, col):
    return 0 <= row < 5 and 0 <= col < 5


def next_position(row, col, command):
    if command== "left":
        col -=1
    elif command == "right":
        col +=1
    elif command == "up":
        row -=1
    elif command == "down":
        row +=1
    return row, col

presents_total = int(input())
size_neigh = int(input())
matrix = []
santa_row = 0
santa_col = 0
nice_kids_counter = 0
for r in range(size_neigh):
    next_row = input().split()
    matrix.append(next_row)
    for c in range(size_neigh):
        if matrix[r][c] == "S":
            santa_col = c
            santa_row = r
        elif matrix[r][c] == "V":
            nice_kids_counter += 1

kids_w_presents = 0
current_row = santa_row
current_col = santa_col
while presents_total>0:
    command = input()
    if command == "Christmas morning":
        break
    new_row, new_col = next_position(current_row, current_col, command)
    if is_inside(new_row, new_col):

        if matrix[new_row][new_col] == "V":
            matrix[new_row][new_col] = "S"
            matrix[current_row][current_col] = "-"
            nice_kids_counter -= 1
            presents_total -= 1
            kids_w_presents += 1
            if presents_total <= 0:
                break
        elif matrix[new_row][new_col] == "C":
            matrix[new_row][new_col] = "S"
            matrix[current_row][current_col] = "-"
            if is_inside(new_row, new_col - 1) and \
                    (matrix[new_row][new_col - 1] == "X" or matrix[new_row][new_col - 1] == "V"):

                if matrix[new_row][new_col - 1] == "V":
                    nice_kids_counter -= 1
                    kids_w_presents += 1
                matrix[new_row][new_col - 1] = "-"
                presents_total -= 1
                if presents_total <= 0:
                    break
            if is_inside(new_row, new_col + 1) and \
                    (matrix[new_row][new_col + 1] == "X" or matrix[new_row][new_col + 1] == "V"):

                if matrix[new_row][new_col + 1] == "V":
                    nice_kids_counter -= 1
                    kids_w_presents += 1
                matrix[new_row][new_col + 1] = "-"
                presents_total -= 1
                if presents_total <= 0:
                    break

            if is_inside(new_row - 1, new_col) and \
                    (matrix[new_row - 1][new_col] == "X" or matrix[new_row - 1][new_col] ==  "V"):

                if matrix[new_row - 1][new_col] == "V":
                    nice_kids_counter -= 1
                    kids_w_presents += 1
                matrix[new_row - 1][new_col] = "-"
                presents_total -= 1
                if presents_total <= 0:
                    break

            if is_inside(new_row + 1, new_col) and \
                    (matrix[new_row + 1][new_col] == "X" or matrix[new_row + 1][new_col] ==  "V"):

                if matrix[new_row + 1][new_col] == "V":
                    nice_kids_counter -= 1
                    kids_w_presents += 1
                matrix[new_row + 1][new_col] = "-"
                presents_total -= 1
                if presents_total <= 0:
                    break
        matrix[new_row][new_col] = "S"
        matrix[current_row][current_col] = "-"
        current_row, current_col = new_row, new_col


if presents_total<=0 and nice_kids_counter !=0:
    print("Santa ran out of presents!")

for r in matrix:
    print(*r, sep=" ")
if nice_kids_counter == 0:
    print(f"Good job, Santa! {kids_w_presents} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_counter} nice kid/s.")
