from collections import deque

boxes = [int(x) for x in input().split()]
magics = deque([int(x) for x in input().split()])
gifts_magic = {150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}
crafted_gifts = {}
is_successful = False
while boxes and magics:
    box = boxes.pop()
    magic = magics.popleft()
    result = box * magic
    if result in gifts_magic:
        if gifts_magic[result] not in crafted_gifts:
            crafted_gifts[gifts_magic[result]] = 0
        crafted_gifts[gifts_magic[result]]+=1
    elif result < 0:
        sum_box_magic = box + magic
        boxes.append(sum_box_magic)
    elif result > 0:
        box += 15
        boxes.append(box)
    else:
        if magic == 0 and box == 0:
            continue
        if magic == 0:
            boxes.append(box)
        elif box == 0:
            magics.appendleft(magic)

if ("Doll" in crafted_gifts and "Wooden train" in crafted_gifts)\
        or ("Teddy bear" in crafted_gifts and "Bicycle" in crafted_gifts):
    is_successful = True

if is_successful:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if boxes:
    print(f"Materials left: {', '.join(str(x) for x in boxes[::-1])}")
if magics:
    print(f"Magic left: {', '.join(str(x) for x in magics)}")
for gift, times in sorted(crafted_gifts.items()):
    print(f"{gift}: {times}")