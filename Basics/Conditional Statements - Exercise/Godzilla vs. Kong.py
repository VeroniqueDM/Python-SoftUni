budget = float(input())
statists = int(input())
clothing_price = float(input())
decor_price = budget*0.1
if statists > 150:
    clothing_price = clothing_price*0.9
clothing_price_total = clothing_price * statists
total_needed = clothing_price_total + decor_price
if total_needed>budget:
    insufficient = total_needed - budget
    print("Not enough money!")
    print(f"Wingard needs {insufficient:.2f} leva more.")
else:
    remaining = budget - total_needed
    print("Action!")
    print(f"Wingard starts filming with {remaining:.2f} leva left.")