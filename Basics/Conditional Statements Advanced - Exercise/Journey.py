budget = float(input())
season = input()
destination = 0
type_of_holiday = 0
money_spent = 0
if budget>1000:
    destination = "Europe"
    type_of_holiday = "Hotel"
    money_spent = budget*0.9
elif 100<budget<=1000:
    destination = "Balkans"
    if season == "summer":
        money_spent = budget*0.4
        type_of_holiday = "Camp"
    elif season == "winter":
        money_spent = budget*0.8
        type_of_holiday = "Hotel"
elif budget<=100:
    destination = "Bulgaria"
    if season == "summer":
        money_spent= budget*0.3
        type_of_holiday = "Camp"
    elif season == "winter":
        money_spent = budget*0.7
        type_of_holiday = "Hotel"
print(f"Somewhere in {destination}")
print(f"{type_of_holiday} - {money_spent:.2f}")
