numbers_sequence = (float(x) for x in input().split())
occ = {}
for num in numbers_sequence:
    if num not in occ:
        occ[num] = 0
    occ[num] += 1

for kvp in occ.items():
    current_num = kvp[0]
    current_num_occ = kvp[1]
    print(f'{current_num:.1f} - {current_num_occ} times')