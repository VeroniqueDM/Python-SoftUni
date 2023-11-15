product = input()
city = input()
amount = float(input())
if city == "Sofia":
    if product == "coffee":
        print(f"{amount*0.5}")
    elif product == "water":
        print(f"{amount * 0.8}")
    elif product == "beer":
        print(f"{amount * 1.2}")
    elif product == "sweets":
        print(f"{amount * 1.45}")
    elif product == "peanuts":
        print(f"{amount * 1.60}")
elif city == "Plovdiv":
    if product == "coffee":
        print(f"{amount*0.4}")
    elif product == "water":
        print(f"{amount * 0.7}")
    elif product == "beer":
        print(f"{amount * 1.15}")
    elif product == "sweets":
        print(f"{amount * 1.30}")
    elif product == "peanuts":
        print(f"{amount * 1.50}")
elif city == "Varna":
    if product == "coffee":
        print(f"{amount*0.45}")
    elif product == "water":
        print(f"{amount * 0.7}")
    elif product == "beer":
        print(f"{amount * 1.10}")
    elif product == "sweets":
        print(f"{amount * 1.35}")
    elif product == "peanuts":
        print(f"{amount * 1.55}")