rows, columns = [int(x) for x in input().split()]
snake_string = input()
idx = 0
matrix = []

for row in range(rows):
    row_elements = []
    for col in range(columns):
        row_elements.append(snake_string[idx%len(snake_string)])
        idx += 1
    if row % 2 == 0:
        matrix.append(row_elements)
    else:
        matrix.append(reversed(row_elements))

for r in range(rows):
    print("".join(matrix[r]))