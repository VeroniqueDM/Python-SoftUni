number_of_cats = int(input())
small_cats = 0
big_cats = 0
enormous_cats = 0
daily_food_total = 0

for cats in range (1, number_of_cats+1):
    food_grams = float(input())
    if 100<= food_grams < 200:
        small_cats +=1

    elif 200<= food_grams <300:
        big_cats +=1

    elif 300<= food_grams < 400:
        enormous_cats +=1
    daily_food_total += food_grams
daily_food_total = daily_food_total/1000
total_price_daily = daily_food_total * 12.45
print(f"Group 1: {small_cats} cats.")
print(f"Group 2: {big_cats} cats.")
print(f"Group 3: {enormous_cats} cats.")
print(f"Price for food per day: {total_price_daily:.2f} lv.")