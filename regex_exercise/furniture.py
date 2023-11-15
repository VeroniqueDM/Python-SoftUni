import re

furniture = input()
regex = r'^>>([a-zA-Z]+)<<(\d+\.?\d*)!(\d+)$'
bought_furniture = []
total_cost = 0
while furniture != "Purchase":
    match = re.findall(regex,furniture)
    if match:
        item = match[0][0]
        price = float(match[0][1]) * float(match[0][2])
        bought_furniture.append(item)
        total_cost += price

    furniture = input()
print("Bought furniture:")
for items in bought_furniture:
    print(items)
print(f"Total money spend: {total_cost:.2f}")
