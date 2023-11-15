quantity = int(input())
days = int(input())
budget = 0
total_spirit = 0
ornament_set_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights_price = 15


for day in range (1, days+1):
    if day%11 == 0:
        quantity +=2
    if day % 2 == 0:
        budget = budget + quantity * ornament_set_price
        total_spirit = total_spirit + 5
    if day % 3 == 0:
        budget = budget + quantity * tree_skirt_price + quantity * tree_garlands_price
        total_spirit += 13
    if day % 5 == 0:
        budget = budget + quantity * tree_lights_price
        total_spirit += 17
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        budget += tree_lights_price + tree_garlands_price + tree_skirt_price

if days%10 == 0:
    total_spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {total_spirit}")

