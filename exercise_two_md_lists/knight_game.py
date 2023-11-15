def is_inside(row, col, size):
    return 0 <= row <size and 0 <= col <size


def collision (row,col,matrix):
    return matrix[row][col] == "K"

def get_attack_counter(horse_row,horse_col, matrix,size):
    collisions = 0
    if is_inside(horse_row-1,horse_col-2,size) and collision(horse_row-1,horse_col-2, matrix):
        collisions+=1
    if is_inside(horse_row+1,horse_col-2,size) and collision(horse_row+1,horse_col-2,matrix):
        collisions += 1
    if is_inside(horse_row-1,horse_col+2,size) and collision(horse_row-1,horse_col+2,matrix):
        collisions += 1
    if is_inside(horse_row+1,horse_col+2,size) and collision(horse_row+1,horse_col+2,matrix):
        collisions += 1
    if is_inside(horse_row+2,horse_col+1,size) and collision(horse_row+2,horse_col+1,matrix):
        collisions += 1
    if is_inside(horse_row-2,horse_col-1,size) and collision(horse_row-2,horse_col-1,matrix):
        collisions += 1
    if is_inside(horse_row+2,horse_col-1,size) and collision(horse_row+2,horse_col-1,matrix):
        collisions += 1
    if is_inside(horse_row-2,horse_col+1,size) and collision(horse_row-2,horse_col+1,matrix):
        collisions += 1
    return collisions



size = int(input())
matrix = [[x for x in list(input())] for _ in range(size)]

horse_coordinates = []


removed_knights = 0

while True:
    table = {}
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == "K":
                counter = get_attack_counter(r,c,matrix,size)
                if counter>0:
                    table[(r, c)] = counter
            else:
                continue
    best_counter = 0
    best_row, best_col = 0, 0
    for coords, counts in table.items():
        if counts > best_counter:
            best_counter = counts
            best_row = coords[0]
            best_col = coords[1]

    matrix[best_row][best_col] = "0"

    if len(table) == 0:
        break
    else:
        removed_knights += 1



print(removed_knights)




