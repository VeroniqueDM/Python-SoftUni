import math
def is_valid(row, col, size):
    return 0 <= row < size, 0 <= col < size

size_mat = int(input())
matrix = []
for row in range(size_mat):
    current_row = input().split()
    matrix.append(current_row)
    for ind in range(size_mat):
        if matrix[row][ind] == "P":
            player_row, player_col = row, ind

coins = 0
player_path = [[player_row, player_col]]
hit_wall = False
while coins < 100:
    command = input()
    if command == "up":
        if player_row == 0:
            player_row = size_mat - 1
        else:
            player_row -= 1

    elif command == "down":
        if player_row == size_mat - 1:
            player_row = 0
        else:
            player_row +=1
    elif command == "right":
        if player_col == size_mat -1:
            player_col = 0
        else:
            player_col +=1
    elif command == "left":
        if player_col == 0:
            player_col = size_mat -1
        else:
            player_col -= 1
    if matrix[player_row][player_col].isdigit() :
        coins += int(matrix[player_row][player_col])
        matrix[player_row][player_col] = "-"
        player_path.append([player_row,player_col])
    elif matrix[player_row][player_col] == "X":
        hit_wall = True
        player_path.append([player_row, player_col])
        break
    else:
        player_path.append([player_row, player_col])

if hit_wall:
    coins = math.floor(coins * 50/100)
    print(f"Game over! You've collected {coins} coins.")
else:
    print(f"You won! You've collected {coins} coins.")

print("Your path:")
print(*player_path, sep="\n")