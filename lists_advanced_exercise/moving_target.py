
targets_int = [int(x) for x in input().split()]

command = input()

def shoot_target(targets, current_index, current_value):
    targets[current_index] -= current_value
    if targets[current_index] <= 0:
        targets.pop(current_index)
    return targets

def add_target(targets, current_index, current_value):
    targets.insert(current_index, current_value)
    return targets


def strike_target(targets, current_index, radius):
    targets = targets[0:current_index-radius] + targets[current_index+radius+1::]
    return targets



while command != "End":
    command_str = command.split()
    action = command_str[0]
    index = int(command_str[1])
    power_rad = int(command_str[2])
    if action == "Shoot" :
        if 0 <= index < len(targets_int):
            targets_int = shoot_target(targets_int, index, power_rad)


    elif action == "Add":
        if 0 <= index < len(targets_int):
            targets_int = add_target(targets_int, index, power_rad)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        if 0 <= index+power_rad < len(targets_int) and 0 <= index-power_rad < len(targets_int):
            targets_int = strike_target(targets_int, index, power_rad)
        else:
            print("Strike missed!" )

    command = input()


targets_string = [str(x) for x in targets_int]
res = "|".join(targets_string)
print(res)