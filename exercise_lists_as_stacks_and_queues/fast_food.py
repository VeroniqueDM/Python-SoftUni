from collections import deque
food_total = int(input())

orders = deque([int(x) for x in input().split()])

max_order = max(orders)
print(max_order)

while orders:
    current_order = orders[0]
    if current_order >food_total:
        break
    food_total -= current_order
    orders.popleft()
if orders:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")
else:
    print("Orders complete")