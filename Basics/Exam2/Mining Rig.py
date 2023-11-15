video_card_price = int(input())
transmitter_price = int(input())
electricity_price_per_day = float(input())
winnings_per_day = float(input())
other_components = 1000
total_money_needed = video_card_price *13 + transmitter_price * 13 + other_components

winnings_per_day = (winnings_per_day - electricity_price_per_day) * 13


import math

days_needed = total_money_needed / winnings_per_day

print(total_money_needed)
print(math.ceil(days_needed))
