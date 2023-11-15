number_of_mines = int(input())

for i in range (1, number_of_mines+1):
    expected_gold_pday = float(input())
    days_on_location = int(input())
    location_total = 0
    for days in range (1, days_on_location +1):
        daily_gold = float(input())
        location_total += daily_gold
    expected_gold_total = expected_gold_pday * days_on_location
    average_location = location_total/days_on_location
    if expected_gold_pday <= average_location:
        print(f"Good job! Average gold per day: {location_total/days_on_location:.2f}.")
    else:
        print(f"You need {expected_gold_pday - average_location:.2f} gold.")
