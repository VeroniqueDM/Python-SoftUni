days_away = int(input())
food = int(input())
deer_one_daily = float(input())
deer_two_daily = float(input())
deer_three_daily = float(input())
total_food_needed = deer_one_daily*days_away + deer_two_daily*days_away +deer_three_daily*days_away
import math
if total_food_needed>food:
    print(f"{math.ceil(total_food_needed-food)} more kilos of food are needed.")
elif food>=total_food_needed:
    print(f"{math.floor(food-total_food_needed)} kilos of food left.")

