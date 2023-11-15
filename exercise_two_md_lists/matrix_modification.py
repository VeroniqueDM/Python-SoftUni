def is_inside(row,col,size_row, size_col):
    return 0 <= row <size_row and 0 <= col < size_col

def calculation(row,col,act,value,matrix):
    if act == "Add":
        matrix[row][col] += value
    elif act == "Subtract":
        matrix[row][col] -= value
    return matrix


rows = int(input())
matrix = []
for _ in range(rows):
    new_list = [int(x) for x in input().split()]
    matrix.append(new_list)

command = input()
new_matrix = []
while command != "END":
    action, row, column, value = command.split()
    if not is_inside(int(row),int(column),len(matrix), len(matrix[0])):
        print("Invalid coordinates")
    else:
        calculation(int(row),int(column),action,int(value),matrix)
    command = input()

for r in matrix:
    print(*r, sep=" ")