def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."
    basket = 0
    products = []
    for product, info in kwargs.items():
        current_price = info[0]
        current_amount = info[1]
        total_price = current_price*current_amount
        if total_price< budget:
            budget -= total_price
            basket +=1
            products.append(f"You bought {product} for {total_price:.2f} leva.")
        else:
            continue
        if basket == 5:
            break
    return "\n".join(products)

print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))



