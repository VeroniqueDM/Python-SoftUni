items_collection = input()
items_list = items_collection.split("|")

budget = float(input())
needed_budget = 150
new_budget = 0
sold_items = ""
profit = 0
for item in range (0, len(items_list)):
    current_item = items_list[item].split("->")
    item = current_item[0]
    price = float(current_item[1])
    if price <= budget:
        if item == "Clothes" and price <= 50:
            budget -= price
            sell_price = price*1.40

            sold_items += f"{sell_price:.2f} "
            new_budget += sell_price
            profit += (sell_price-price)
        elif item == "Shoes" and price <= 35:
            budget -= price
            sell_price = price * 1.40
            sold_items += f"{sell_price:.2f} "
            new_budget += sell_price
            profit += (sell_price-price)

        elif item == "Accesories" and price <= 20.50:
            budget -= price
            sell_price = price * 1.40
            sold_items += f"{sell_price:.2f} "
            new_budget += sell_price
            profit += (sell_price-price)
    else:
        continue

# for items in range (0, len(sold_items)):
#     sold_items[items] = str(sold_items[items])

total_budget = new_budget + budget
#
# join_str = " "
# result = join_str.join(sold_items)
print(sold_items)
print(f"Profit: {profit:.2f}")

if total_budget >= needed_budget:

    print("Hello, France!")
else:
    print("Not enough money.")