from collections import deque

choco_sequence = [int(x) for x in input().split(", ")]
milk_sequence = deque([int(x) for x in input().split(", ")])
milkshakes = 0
while milk_sequence and choco_sequence and milkshakes<5:

    chocolate = choco_sequence.pop()
    milk = milk_sequence.popleft()

    if chocolate<= 0 and milk <=0:
        continue
    if chocolate <= 0:
        milk_sequence.appendleft(milk)
        continue
    if milk <= 0:
        choco_sequence.append(chocolate)
        continue
    if chocolate == milk:
        milkshakes +=1
    else:
        milk_sequence.append(milk)
        chocolate -= 5
        choco_sequence.append(chocolate)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if choco_sequence:
    print(f"Chocolate: {', '.join([str(x) for x in choco_sequence])}")
else:
    print("Chocolate: empty")
if milk_sequence:
    print(f"Milk: {', '.join([str(x) for x in milk_sequence])}")
else:
    print("Milk: empty")