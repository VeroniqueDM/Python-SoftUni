capacity = float(input())
suitcases_count = 0
while capacity > 0:
    command = input()
    if command == "End":
        print("Congratulations! All suitcases are loaded!")
        break
    suitcase_volume = float(command)
    capacity -= suitcase_volume

    if capacity < 0:
        capacity+=suitcase_volume
        print("No more space!")
        break
    suitcases_count += 1
    if suitcases_count%3 == 0:
        capacity = capacity - suitcase_volume*0.1

print(f"Statistic: {suitcases_count} suitcases loaded.")