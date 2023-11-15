clothes_stack = [int(x) for x in input().split()]
rack_capacity = int(input())
racks = 1
current_rack = rack_capacity
while clothes_stack:
    current_item = clothes_stack.pop()
    if current_item <= current_rack:
        current_rack -= current_item
    else:
        racks += 1
        current_rack = rack_capacity
        current_rack -= current_item

print(racks)
