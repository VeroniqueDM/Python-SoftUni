capacity = 255
n = int(input())
total_liters = 0
for lines in range (0, n):
    liters = int(input())
    capacity -= liters
    if capacity < 0:
        print("Insufficient capacity!")
        capacity += liters
        continue
    total_liters +=liters

print(total_liters)
