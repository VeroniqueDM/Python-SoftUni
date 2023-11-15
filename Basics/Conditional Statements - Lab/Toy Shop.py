puzzle_price = 2.60
doll_price = 3.00
bear_price = 4.10
minion_price = 8.20
truck_price = 2.00
excursion_price = float(input())
puzzle_count = int(input())
doll_count = int(input())
bear_count = int(input())
minion_count = int(input())
truck_count = int(input())
toys_order = puzzle_count + doll_count + bear_count + minion_count + truck_count
total_invoice = doll_count * doll_price + bear_count * bear_price + puzzle_count * puzzle_price + minion_count * minion_price + truck_count * truck_price
if toys_order >= 50:
    total_invoice = total_invoice - total_invoice * 0.25
    rent = total_invoice * 0.1
    earned = total_invoice - rent
    if earned >= excursion_price:
        remaining = f"{(earned - excursion_price):.2f}"
        print(f"Yes! {remaining} lv left.")
    else:
        needed = f"{(excursion_price - earned):.2f}"
        print(f"Not enough money! {needed} lv needed.")
else:
    rent = total_invoice * 0.1
    earned = total_invoice - rent
    if earned >= excursion_price:
        remaining = f"{(earned - excursion_price):.2f}"
        print(f"Yes! {remaining} lv left.")
    else:
        needed = f"{(excursion_price - earned):.2f}"
        print(f"Not enough money! {needed} lv needed.")

# xlkl;\
#     kkk
#     lpl
#
