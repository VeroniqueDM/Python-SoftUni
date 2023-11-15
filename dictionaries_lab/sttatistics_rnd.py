command = input()

#     .split(":")
# product_type = new_product[0]
# product_amount = new_product[1]
current_stock = {}

while command != "statistics":
    new_product = command.split(":")
    product_type = new_product[0]
    product_amount = new_product[1]
    if product_type not in current_stock:
        current_stock[product_type] = int(product_amount)
    else:
        current_stock[product_type] += int(product_amount)
    command = input()

print("Products in stock:")
for k in current_stock:
    print(f"- {k}: {current_stock[k]}")

print(f"Total Products: {len(current_stock)}")

sum_values = 0
for val in current_stock.values():
    sum_values += val

print(f"Total Quantity: {sum_values}")