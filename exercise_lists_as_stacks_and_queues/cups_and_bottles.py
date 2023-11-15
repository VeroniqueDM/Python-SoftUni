from collections import deque

cups = deque(int(x) for x in input().split())
bottles = [int(y) for y in input().split()]
wasted_water = 0
while bottles:
    current_bottle = bottles.pop()
    current_cup = cups.popleft()
    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
    else:
        current_cup -= current_bottle
        cups.appendleft(current_cup)
    if not cups:
        break

if cups:
    print('Cups:', end=" ")
    while cups:
        print(cups.popleft(), end=" ")
elif bottles:
    print('Bottles:', end=" ")
    while bottles:
        print(bottles.pop(), end=" ")

print(f'\nWasted litters of water: {wasted_water}')