stock_args = input().split()
products_to_check = input().split()
table = {}

for i in range (0, len(stock_args), 2):
    product = stock_args[i]
    amount = int(stock_args[i + 1])
    table[product] = amount

for current_product in products_to_check:
    if current_product not in stock_args:
        print(f"Sorry, we don't have {current_product}")
    else:

        current_amount = table[current_product]
        print(f"We have {current_amount} of {current_product} left")