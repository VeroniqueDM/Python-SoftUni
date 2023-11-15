n = int(input())

matrix = [[x for x in input()] for y in range(n)]

sym = input()
is_true = False
for i in range(n):
    for j in range(n):
        if sym == matrix[i][j]:
            is_true = True
            print(f"({i}, {j})")
            break
    if is_true:
        break

if not is_true:
    print(f"{sym} does not occur in the matrix")
