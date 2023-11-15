row, column = [int(x) for x in input().split()]
palindrome_matrix = []

for row_ind in range(row):
    current_row = []
    for col_ind in range(column):
        first_last_letter = chr(97+row_ind)
        middle_letter = chr(97+row_ind+col_ind)
        word = first_last_letter +middle_letter+first_last_letter
        current_row.append(word)
    palindrome_matrix.append(current_row)

for r in range(row):
    for c in range(column):
        print(palindrome_matrix[r][c], end=" ")
    print()
