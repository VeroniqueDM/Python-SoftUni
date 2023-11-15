type_of_flowers = input()
flowers_count = int(input())
budget = int(input())
price = 0
if type_of_flowers == "Roses":
    price = flowers_count * 5
    if flowers_count >80:
        price = price*0.9
elif type_of_flowers == "Dahlias":
    price = flowers_count *3.80
    if flowers_count>90:
        price = price*0.85
elif type_of_flowers == "Tulips":
    price = flowers_count * 2.8
    if flowers_count>80:
        price = price*0.85
elif type_of_flowers == "Narcissus":
    price = flowers_count *3
    if flowers_count<120:
        price= price*1.15
elif type_of_flowers == "Gladiolus":
    price = flowers_count*2.5
    if flowers_count<80:
        price = price*1.20

if price>budget:
    print(f"Not enough money, you need {(price-budget):.2f} leva more.")
else:
    print(f"Hey, you have a great garden with {flowers_count} {type_of_flowers} and {(budget-price):.2f} leva left.")