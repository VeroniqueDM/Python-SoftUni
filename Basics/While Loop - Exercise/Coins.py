change = float(input())
counter = 0
change_to_coins = int(change*100)
# 200
# 100
# 50
# 20
# 10
# 5
# 2
# 1
while change_to_coins >=1:
    if change_to_coins>=200:
        change_to_coins = change_to_coins - 200
        counter = counter + 1
    elif change_to_coins >= 100:
        change_to_coins = change_to_coins - 100
        counter = counter + 1
    elif change_to_coins >= 50:
        change_to_coins = change_to_coins - 50
        counter = counter + 1
    elif change_to_coins >= 20:
        change_to_coins = change_to_coins - 20
        counter = counter + 1
    elif change_to_coins >= 10:
        change_to_coins = change_to_coins - 10
        counter = counter + 1
    elif change_to_coins >= 5:
        change_to_coins = change_to_coins - 5
        counter = counter + 1
    elif change_to_coins >= 2:
        change_to_coins = change_to_coins - 2
        counter = counter + 1
    elif change_to_coins >= 1:
        change_to_coins = change_to_coins - 1
        counter = counter + 1
print(counter)