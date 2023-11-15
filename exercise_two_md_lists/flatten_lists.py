matrix = [[int(x) for x in a.split()] for a in input().split("|")]
reverse_list = []

for r in range(len(matrix)):
    sublist = matrix.pop()
    reverse_list.extend(sublist)

print(*reverse_list, sep=" ")

