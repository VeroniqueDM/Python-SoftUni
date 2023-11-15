budget = float(input())
price_of_kg_flour = float(input())
price_of_pack_eggs = 75/100 * price_of_kg_flour
price_of_lt_milk = 1.25 * price_of_kg_flour
price_of_qt_milk = 0.25 * price_of_lt_milk
colored_eggs = 0
number_of_breads = 0
price_of_bread = price_of_qt_milk + price_of_pack_eggs +price_of_kg_flour

while budget> price_of_bread:
    number_of_breads += 1
    budget -= price_of_bread
    colored_eggs += 3
    if number_of_breads%3 == 0:
        colored_eggs -= (number_of_breads - 2)

print(f"You made {number_of_breads} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")