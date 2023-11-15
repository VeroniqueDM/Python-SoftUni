n = int(input())
parking_lot = set()
for _ in range(n):
    direction, car_number = input().split(", ")
    if direction == "IN":
        parking_lot.add(car_number)
    else:
        parking_lot.remove(car_number)
if parking_lot:
    for cars in  parking_lot:
        print(cars)
else:
    print("Parking Lot is Empty")