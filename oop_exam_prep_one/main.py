from project.bakery import Bakery

bakery = Bakery('Random')

print(bakery.add_food('Cake', 'Carrot Cake', 3.4))
print(bakery.add_food('Cake', 'Choco Cake', 3.4))
print(bakery.add_food('Bread', 'Carrot Bread', 3.4))
print(bakery.add_drink('Tea','White tea', 300, 'ENG TEA'))
print(bakery.add_table('InsideTable', 20, 5))
print(bakery.add_table('OutsideTable', 60, 5))
print(bakery.reserve_table(2))
print(bakery.order_food(20,'Carrot Cake','Choco Cake', 'Carrot Bread', 'pancakes' ))