from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])

gifts = {"Gemstone":0, "Porcelain Sculpture":0, "Gold":0, "Diamond Jewellery":0}

while materials and magic_levels:
    material = materials.pop()
    magic = magic_levels.popleft()
    result = material + magic
    if result < 100:
        if result % 2 == 0:
            result = material *2 + magic * 3
        else:
            result *= 2
    elif result > 499:
        result /=2
    elif 100 <= result <= 199:
        gifts["Gemstone"] +=1
    elif 200 <= result <= 299:
        gifts["Porcelain Sculpture"] +=1
    elif 300 <= result <= 399:
        gifts["Gold"] +=1
    elif 400 <= result <= 499:
        gifts["Diamond Jewellery"] +=1

if (gifts["Gemstone"] > 0 and gifts["Porcelain Sculpture"]>0 ) or (gifts["Gold"] >0 and gifts["Diamond Jewellery"]>0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in materials)}")

for k,v in sorted(gifts.items()):
    if v>0:
        print(f"{k}: {v}")