beginning = int(input())
ending = int(input())
magic_number = int(input())
counter = 0
hit = 0
for x1 in range (beginning, ending + 1):
    if hit == 1:
        break
    for x2 in range (beginning, ending + 1):
        if x1 + x2 != magic_number:
            counter += 1
        else:
            hit = 1
            counter += hit
            print(f"Combination N:{counter} ({x1} + {x2} = {magic_number})")
            break
if hit == 0:
    print(f"{counter} combinations - neither equals {magic_number}")