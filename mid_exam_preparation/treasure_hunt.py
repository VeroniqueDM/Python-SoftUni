treasure_chest = input().split("|")
command = input().split()
activity = command[0]

while activity != "Yohoho!":
    if activity == "Loot":
        for i in range (1, len(command)):
            if command[i] not in treasure_chest:
                treasure_chest.insert(0, command[i])
    elif activity == "Drop":

        index = int(command[1])
        if 0<=index < len(treasure_chest):
            removed_item = treasure_chest.pop(index)
            treasure_chest.append(removed_item)

        else:
            command = input().split()
            activity = command[0]
            continue
    elif activity == "Steal":
        count = int(command[1])
        removed_item = treasure_chest[-count:]
        print(", ".join(removed_item))
        treasure_chest = treasure_chest[:-count]

    command = input().split()
    activity = command[0]

if len(treasure_chest) == 0:
    print("Failed treasure hunt.")
else:
    sum_lengths = 0
    for a in treasure_chest:
        item = list(a)
        word_length = len(item)
        sum_lengths += word_length

    average = sum_lengths / len(treasure_chest)

    print(f"Average treasure gain: {average:.2f} pirate credits.")