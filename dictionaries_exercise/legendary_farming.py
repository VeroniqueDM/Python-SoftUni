command = input().split()
materials_dict = {"fragments":0, "shards": 0, "motes":0}
scrap_dict = {}
limit = 250

is_obtained = False

while command:
    for val in range(0, len(command), 2):
        quantity = int(command[val])
        material = command[val + 1].lower()
        if material == "shards" or material == "fragments" or material == "motes":
            if material not in materials_dict:
                materials_dict[material] = 0
            materials_dict[material] += quantity
            for i, v in materials_dict.items():
                if v >= 250:
                    if i == "shards":
                        materials_dict[i] -=250
                        is_obtained = True
                        print("Shadowmourne obtained!")

                        break
                    elif i == 'fragments':
                        materials_dict[i] -= 250
                        is_obtained = True
                        print("Valanyr obtained!")
                        break
                    elif i == "motes":
                        materials_dict[i] -= 250
                        is_obtained = True
                        print("Dragonwrath obtained!")
                        break
            if is_obtained == True:
                break
        else:
            if material not in scrap_dict:
                scrap_dict[material] = 0
            scrap_dict[material] += quantity
    if is_obtained == True:
        break
    command = input().split()




res_materials = dict(sorted(materials_dict.items(), key=lambda x:(-x[1], x[0])))
res_scrap = dict(sorted(scrap_dict.items(), key=lambda y:y[0]))

for a,b in res_materials.items():
    print(f"{a}: {b}")
for c,d in res_scrap.items():
    print(f"{c}: {d}")





