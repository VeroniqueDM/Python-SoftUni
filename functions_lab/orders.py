

def bill(product, amount):
    price_product = 0
    if product == "coffee":
        price_product = 1.50
    elif product == "water":
        price_product = 1.00
    elif product == "coke":
        price_product = 1.40
    elif product == "snacks":
        price_product = 2.00
    total_price = price_product * amount
    return total_price

product_name = input()
amount_quantity = int(input())
result = bill(product_name, amount_quantity)

print(f"{result:.2f}")