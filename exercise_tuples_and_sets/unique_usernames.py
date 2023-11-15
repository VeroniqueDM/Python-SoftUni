n = int(input())
users_set = set()
for _ in range(n):
    username = input()
    users_set.add(username)

for user in users_set:
    print(user)