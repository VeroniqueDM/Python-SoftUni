rows = int(input())

even_matrix = [[int(x) for x in input().split(", ") if int(x)%2 == 0] for i in range(rows)]

print(even_matrix)