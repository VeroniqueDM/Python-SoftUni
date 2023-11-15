n = int(input())
periodic_table = set()
for _ in range(n):
    compounds = input().split()
    for c_element in compounds:
        periodic_table.add(c_element)
#   periodic_table = periodic_table.union(compounds)

for elem in periodic_table:
    print(elem)