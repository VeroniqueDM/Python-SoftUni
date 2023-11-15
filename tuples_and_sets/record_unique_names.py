n = int(input())
names_set = set()
for _ in range(n):
    name = input()
    if name not in names_set:
        names_set.add(name)

for person in names_set:
    print(person)