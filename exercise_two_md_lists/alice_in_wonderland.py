def is_inside(row, col, size):
    return 0<=row<size and 0<=col<size

def next_cell(row, col, command):
    if command == "right":
        return row, col +1
    elif command == "left":
        return row, col -1
    elif command == "up":
        return row-1, col
    elif command == "down":
        return row+1, col


size_mat = int(input())
matrix = []
alice_row = 0
alice_col = 0
for row in range(size_mat):
    current_row = input().split()
    matrix.append(current_row)
    for col in range(size_mat):
        if matrix[row][col] == "A":
            alice_row = row
            alice_col = col
            matrix[row][col] = "*"
next_row = alice_row
next_col = alice_col
bags = 0
while True:
    command = input()
    next_row,next_col = next_cell(next_row,next_col,command)
    if not is_inside(next_row,next_col,size_mat):
        break
    if matrix[next_row][next_col] == "R":
        matrix[next_row][next_col] = "*"
        break
    if matrix[next_row][next_col].isdigit():
        bags += int(matrix[next_row][next_col])
    matrix[next_row][next_col] = "*"
    if bags >=10:
        break

if bags >= 10 :
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for r in matrix:
    print(*r, sep= " ")
