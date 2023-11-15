number_of_cities = int(input())
profit = 0
city_counter = 0
for i in range(0, number_of_cities):
    city_name = input()
    money_earned = float(input())
    money_spent = float(input())
    city_counter += 1

    if city_counter % 3 == 0 and city_counter % 5 != 0:
        money_spent += money_spent * 0.5

    elif city_counter % 5 == 0:
        money_earned -= money_earned * 0.1


    current_profit = money_earned - money_spent
    profit += current_profit
    print(f"In {city_name} Burger Bus earned {current_profit:.2f} leva.")

print(f"Burger Bus total profit: {profit:.2f} leva.")
