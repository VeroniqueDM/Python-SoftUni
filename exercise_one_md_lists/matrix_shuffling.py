rows, columns = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]
command = input()
while not command == "END":
    action = command.split()
    if len(action) != 5:
        print("Invalid input!")
        command = input()
        continue
    r_ts = int(action[1])
    c_ts = int(action[2])
    r_s = int(action[3])
    c_s = int(action[4])
    if action[0] != "swap" \
            or not (0 <= r_ts and r_s < rows) or not (0 <= c_ts and c_s < columns):
        print("Invalid input!" )
        command = input()
        continue

    matrix[r_ts][c_ts], matrix[r_s][c_s] = matrix[r_s][c_s], matrix[r_ts][c_ts]
    for i in range(rows):
        print(" ".join(matrix[i]))
    command = input()