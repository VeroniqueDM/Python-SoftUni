from collections import deque

bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings = [int(x) for x in input().split(", ")]
# cherry_bombs = 0
# datura_bombs = 0
# smoked_bombs = 0
pouch_filled = False
bombs_info = {40: "Datura Bombs",
              60: "Cherry Bombs",
              120: "Smoked Decoy Bombs"}
my_pouch = {"Cherry Bombs": 0,
            "Datura Bombs":0,
            "Smoked Decoy Bombs":0}
while bomb_effects and bomb_casings:
    effect = bomb_effects[0]
    casing = bomb_casings[-1]
    sum_b = effect + casing
    if sum_b in bombs_info:
        my_pouch[bombs_info[sum_b]] += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -=5

    if my_pouch["Cherry Bombs"] >=3 and my_pouch["Datura Bombs"]>=3 and my_pouch["Smoked Decoy Bombs"]>=3:
        pouch_filled = True
        break

if pouch_filled:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
else:
    print("Bomb Effects: empty")
if bomb_casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
else:
    print("Bomb Casings: empty")
print(f"Cherry Bombs: {my_pouch['Cherry Bombs']}")
print(f"Datura Bombs: {my_pouch['Datura Bombs']}")
print(f"Smoke Decoy Bombs: {my_pouch['Smoked Decoy Bombs']}")
