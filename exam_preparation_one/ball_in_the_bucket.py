def is_valid(row,col):
    return 0<=row<6 and 0 <=col<6
matrix = [input().split() for _ in range(6)]
points = 0
for _ in range(3):
    row, column = [int(x) for x in eval(input())]
    if is_valid(row,column):
        if matrix[row][column] == "B":
            sum_col = 0
            matrix[row][column] = 0
            for a in range(6):
                sum_col += int(matrix[a][column])
            points +=sum_col

if points < 100:
    print(f"Sorry! You need {100-points} points more to win a prize.")
elif 100 <= points <=199:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif 199< points < 300:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
elif 299< points:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")