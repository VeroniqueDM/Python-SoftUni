from collections import deque
pizza_orders = deque(int(x) for x in input().split(", "))
employees_cap = [int(x) for x in input().split(", ")]
total_pizzas = 0
while pizza_orders:
    if not employees_cap:
        break
    current_pizza = pizza_orders.popleft()
    if current_pizza > 10 or current_pizza <=0:
        continue

    current_employee = employees_cap.pop()
    if current_pizza > current_employee:
        leftover = current_pizza - current_employee
        pizza_orders.appendleft(leftover)
        total_pizzas += current_employee
    else:
        total_pizzas += current_pizza

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f'Total pizzas made: {total_pizzas}')
    print(f'Employees: {", ".join(str(x) for x in employees_cap)}')
else:
    print("Not all orders are completed.")
    print(f'Orders left: {", ".join(str(x) for x in pizza_orders)}')

