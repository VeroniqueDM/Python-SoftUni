items_collection = input()
items_list = items_collection.split("|")

budget = float(input())
needed_budget = 150
new_budget = 0
sold_items = []
profit = 0
for item in range (0, len(items_list)):
    current_item = items_list[item].split("->")
    item = current_item[0]
    price = float(current_item[1])
    if price <= budget:
        if item == "Clothes" and price <= 50:
            budget -= price
            sell_price = price*1.40
            sold_items.append(sell_price)
            new_budget += sell_price
            profit += (sell_price-price)
        elif item == "Shoes" and price <= 35:
            budget -= price
            sell_price = price * 1.40
            sold_items.append(sell_price)
            new_budget += sell_price
            profit += (sell_price-price)

        elif item == "Accessories" and price <= 20.50:
            budget -= price
            sell_price = price * 1.40
            sold_items.append(sell_price)
            new_budget += sell_price
            profit += (sell_price-price)
    else:
        continue


total_budget = new_budget + budget

for i in sold_items:
    print(f"{i:.2f}", end=" ")
print()
# print(" ".join(sold_items))
print(f"Profit: {profit:.2f}")

if total_budget >= needed_budget:
    print("Hello, France!")
else:
    print("Not enough money.")