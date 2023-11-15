command = input()

shopping_cart = {}

while command != "buy":
    new_product = command.split()
    product = new_product[0]
    price = float(new_product[1])
    quantity = int(new_product[2])
    if product not in shopping_cart:
        shopping_cart[product] = {"current_price": 0, "current_quantity":0}

    shopping_cart[product]["current_price"] = price
    shopping_cart[product]["current_quantity"] += quantity

    command = input()

res = {}
for k, v in shopping_cart.items():

    total_price = v["current_price"] * v["current_quantity"]
    res[k] = total_price

for pro,pri in res.items():
    print(f"{pro} -> {pri:.2f}")


