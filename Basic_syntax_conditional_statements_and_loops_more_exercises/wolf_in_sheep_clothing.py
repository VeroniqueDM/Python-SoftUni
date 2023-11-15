list_animals = input().split(", ")
#
# wolf = list_animals.index("wolf")

if list_animals[-1]  == "wolf":
    print("Please go away and stop eating my sheep")
else:
    reverse_list = list(reversed(list_animals))
    wolf = reverse_list.index("wolf")
    sheep = wolf
    print(f"Oi! Sheep number {sheep}! You are about to be eaten by a wolf!" )