def is_valid(row,col):
    return 0<=row<8 and 0<=col<8

matrix = [[x for x in input().split()] for _ in range(8)]

white_row = 0
white_col = 0
black_row = 0
black_col = 0

for r in range(8):
    for c in range(8):
        if matrix[r][c] == "w":
            white_row = r
            white_col = c
        elif matrix[r][c] == "b":
            black_col = c
            black_row = r
game_won_white = False
game_won_black = False
white_captured = False
black_captured = False
for turn in range(20):
    if turn %2 == 0:
        if is_valid(white_row-1,white_col-1) and matrix[white_row-1][white_col-1] == "b":
            white_captured = True
            white_row -=1
            white_col -=1
            break
        if is_valid(white_row-1,white_col+1) and matrix[white_row -1][white_col+1] == "b":
            white_captured = True
            white_row -=1
            white_col += 1
            break
    else:

        if is_valid(black_row+1,black_col-1) and matrix[black_row+1][black_col-1] == "w" :
            black_captured = True
            black_row += 1
            black_col -= 1
            break
        if is_valid(black_row+1, black_col+1) and matrix[black_row+1][black_col+1] == "w":
            black_captured = True
            black_row += 1
            black_col +=1
            break

    if turn % 2 == 0:
        matrix[white_row][white_col] = "-"
        white_row -= 1
        matrix[white_row][white_col] = "w"
    else:
        matrix[black_row][black_col] = "-"
        black_row += 1
        matrix[black_row][black_col] = "b"
    if white_row == 0:
        game_won_white = True
        break
    if black_row == 7:
        game_won_black = True
        break


rows = {0:"8", 1:"7", 2:"6", 3:"5", 4:"4", 5: "3", 6:"2", 7:"1"}
cols = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5: "f", 6:"g", 7:"h"}

if white_captured:
    print(f"Game over! White win, capture on {cols[white_col]}{rows[white_row]}.")
elif black_captured:
    print(f"Game over! Black win, capture on {cols[black_col]}{rows[black_row]}.")
elif game_won_white:
    print(f"Game over! White pawn is promoted to a queen at {cols[white_col]}{rows[white_row]}.")
elif game_won_black:
    print(f"Game over! Black pawn is promoted to a queen at {cols[black_col]}{rows[black_row]}.")

