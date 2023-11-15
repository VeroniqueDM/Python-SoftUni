def is_inside(row, col, size_row, size_col):
    return 0<= row < size_row and 0<=col<size_col


def next_index(row, col, command):
    if command == "L":
        return row, col -1
    elif command == "R":
        return row, col +1
    elif command == "U":
        return row-1, col
    elif command == "D":
        return row+1, col


rows, columns = [int(x) for x in input().split()]
matrix_bunnies = [list(input()) for _ in range(rows)]
directions = list(input())

player_row = 0
player_col = 0
bunnies = set()
for r in range(rows):
    for c in range(columns):
        if matrix_bunnies[r][c] == "P":
            player_row, player_col = r, c
        elif matrix_bunnies[r][c] == "B":
            bunnies.add(f'{r} {c}')
won = False
dead = False
matrix_bunnies[player_row][player_col] = "."
for command in directions:
    new_player_row, new_player_col = next_index(player_row,player_col,command)
    if not is_inside(new_player_row,new_player_col,rows,columns):
        won = True

    elif matrix_bunnies[new_player_row][new_player_col] == "B":
        dead = True
        player_row, player_col = new_player_row, new_player_col
    else:
        player_row, player_col = new_player_row, new_player_col
    new_bunnies = set()
    for bunny in bunnies:
        bunny_row, bunny_col = [int(x) for x in bunny.split()]
        if is_inside(bunny_row-1,bunny_col, rows, columns):
            matrix_bunnies[bunny_row -1][bunny_col] = "B"
            new_bunnies.add(f"{bunny_row -1} {bunny_col}")
        if is_inside(bunny_row, bunny_col-1, rows, columns):
            matrix_bunnies[bunny_row ][bunny_col-1] = "B"
            new_bunnies.add(f"{bunny_row} {bunny_col-1}")
        if is_inside(bunny_row , bunny_col+1, rows, columns):
            matrix_bunnies[bunny_row ][bunny_col+1] = "B"
            new_bunnies.add(f"{bunny_row} {bunny_col+1}")
        if is_inside(bunny_row + 1, bunny_col, rows, columns):
            matrix_bunnies[bunny_row + 1][bunny_col] = "B"
            new_bunnies.add(f"{bunny_row +1} {bunny_col}")
    bunnies = bunnies.union(new_bunnies)
    if matrix_bunnies[player_row][player_col] == "B":
        dead = True
    if dead or won:
        break

for r in matrix_bunnies:
    print(*r, sep="")

if won:
    print(f'won: {player_row} {player_col}')
else:
    print(f'dead: {player_row} {player_col}')