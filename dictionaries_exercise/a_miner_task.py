resource = input()


stock_resources = {}

while resource != "stop":
    amount = int(input())
    if resource not in stock_resources:
        stock_resources[resource] = 0
    stock_resources[resource] += amount
    resource = input()


for items in stock_resources:
    print(f"{items} -> {stock_resources[items]}")