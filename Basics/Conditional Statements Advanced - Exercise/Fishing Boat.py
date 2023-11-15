budget = int(input())
season = input()
fishermen = int(input())
rent = 0
if season == "Summer" or season == "Autumn":
    rent = 4200
    if fishermen <= 6:
        rent = rent * 0.9
    elif 6 < fishermen <= 11:
        rent = rent * 0.85
    elif fishermen > 11:
        rent = rent * 0.75
elif season == "Spring":
    rent = 3000
    if fishermen <= 6:
        rent = rent * 0.9
    elif 6 < fishermen <= 11:
        rent = rent * 0.85
    elif fishermen > 11:
        rent = rent * 0.75
elif season == "Winter":
    rent = 2600
    if fishermen <= 6:
        rent = rent * 0.9
    elif 6 < fishermen <= 11:
        rent = rent * 0.85
    elif fishermen > 11:
        rent = rent * 0.75
if season != "Autumn" and fishermen % 2==0:
    rent = rent * 0.95
if budget >= rent:
    print(f"Yes! You have {(budget - rent):.2f} leva left.")
else:
    print(f"Not enough money! You need {(rent - budget):.2f} leva.")
