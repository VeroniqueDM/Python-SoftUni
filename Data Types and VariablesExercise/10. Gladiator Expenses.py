lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_expenses = 0
shields_counter = 0
for fights in range (1, lost_fights + 1):
    if fights%2 == 0:
        total_expenses += helmet_price
    if fights%3 == 0:
        total_expenses += sword_price
        if fights%2 == 0:
            total_expenses += shield_price
            shields_counter += 1
            if shields_counter%2 == 0 and shields_counter != 0:
                total_expenses += armor_price

print(f"Gladiator expenses: {total_expenses:.2f} aureus")

# Without for-loop:
# total_helmets_broken = lost_fights // 2
# total_swords_broken = lost_fights // 3
# total_shields_broken = lost_fights // 6
# total_armor_broken = total_shields_broken // 2
