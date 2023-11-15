def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = int(input())
commands = input().split()
mining_matrix = [[x for x in input().split()] for _ in range(size)]
miner_position = []
for r in range(size):
    for c in range(size):
        if mining_matrix[r][c] == "s":
            miner_position = [r, c]
            break
    if miner_position:
        break
remaining_coal = 0
for a in range(size):
    for b in range(size):
        if mining_matrix[a][b] == "c":
            remaining_coal +=1
miner_row = miner_position[0]
miner_col = miner_position[1]
stepped_on_e = False
for com in commands:
    if com == "left":
        if is_valid(miner_row,miner_col-1, size):
            miner_col -= 1
            if mining_matrix[miner_row][miner_col] == "*":
                continue
            elif mining_matrix[miner_row][miner_col] == "c":
                remaining_coal -= 1
                mining_matrix[miner_row][miner_col] = "*"
            elif mining_matrix[miner_row][miner_col] == "e":
                stepped_on_e = True
                print(f"Game over! ({miner_row}, {miner_col})")
                break
        else:
            continue
    elif com == "right":
        if is_valid(miner_row, miner_col + 1, size):
            miner_col += 1
            if mining_matrix[miner_row][miner_col] == "*":
                continue
            elif mining_matrix[miner_row][miner_col] == "c":
                remaining_coal -= 1
                mining_matrix[miner_row][miner_col] = "*"
            elif mining_matrix[miner_row][miner_col] == "e":
                stepped_on_e = True
                print(f"Game over! ({miner_row}, {miner_col})")
                break
        else:
            continue
    elif com == "up":
        if is_valid(miner_row-1, miner_col, size):
            miner_row -= 1
            if mining_matrix[miner_row][miner_col] == "*":
                continue
            elif mining_matrix[miner_row][miner_col] == "c":
                remaining_coal -= 1
                mining_matrix[miner_row][miner_col] = "*"
            elif mining_matrix[miner_row][miner_col] == "e":
                stepped_on_e = True
                print(f"Game over! ({miner_row}, {miner_col})")
                break
        else:
            continue
    elif com == "down":
        if is_valid(miner_row+1, miner_col, size):
            miner_row += 1
            if mining_matrix[miner_row][miner_col] == "*":
                continue
            elif mining_matrix[miner_row][miner_col] == "c":
                remaining_coal -= 1
                mining_matrix[miner_row][miner_col] = "*"
            elif mining_matrix[miner_row][miner_col] == "e":
                stepped_on_e = True
                print(f"Game over! ({miner_row}, {miner_col})")
                break
        else:
            continue
    if remaining_coal == 0:
        print(f'You collected all coal! ({miner_row}, {miner_col})')
        break

if not stepped_on_e and remaining_coal>0:
    print(f"{remaining_coal} pieces of coal left. ({miner_row}, {miner_col})")

