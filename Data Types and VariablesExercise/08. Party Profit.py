group_size = int(input())
total_days = int(input())

total_coins = 0
for days in range (1, total_days+1):
    if days%10 == 0:
        group_size -= 2
    if days%15 == 0:
        group_size += 5
    total_coins += (50 - 2*group_size)
    if days%3 == 0:
        total_coins -= 3*group_size
    if days%5 == 0:
        total_coins += group_size*20
        if days%3 == 0:
            total_coins -= group_size*2

coins_per_person = int(total_coins / group_size)

print(f"{group_size} companions received {coins_per_person} coins each.")



