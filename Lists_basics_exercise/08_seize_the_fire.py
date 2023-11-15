fire_cells_string = input()
water = int(input())
effort = 0
total_fire = 0
fire_cells_list = fire_cells_string.split("#")
put_out_fires = list()

for fire in range (0, len(fire_cells_list)):

    current_fire = fire_cells_list[fire]
    current_fire_list = current_fire.split(" = ")
    current_fire_type = current_fire_list[0]
    current_cell_value = current_fire_list[1]

    if int(current_cell_value) <= water:
        if current_fire_type == "High":
            if 81 <= int(current_cell_value) <= 125:
                water -= int(current_cell_value)
                effort += int(current_cell_value) * 0.25
                total_fire += int(current_cell_value)
                put_out_fires.append(current_cell_value)


        elif current_fire_type == "Medium":
            if 51 <= int(current_cell_value) <= 80:
                water -= int(current_cell_value)
                effort += int(current_cell_value) * 0.25
                total_fire += int(current_cell_value)
                put_out_fires.append(current_cell_value)


        elif current_fire_type == "Low":
            if 1 <= int(current_cell_value) <= 50:
                water -= int(current_cell_value)
                effort += int(current_cell_value) * 0.25
                total_fire += int(current_cell_value)
                put_out_fires.append(current_cell_value)


    else:
        continue
print("Cells:")
for fires in range (0, len(put_out_fires)):
    print(f" - {put_out_fires[fires]}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")

