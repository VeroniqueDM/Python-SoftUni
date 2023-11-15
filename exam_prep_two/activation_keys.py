raw_key = input()
command = input().split(">>>")

while command[0] != "Generate":
    instruction = command[0]
    if instruction == "Contains":
        substring = command[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")
    elif instruction == "Flip":
        case = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        if case == "Upper":
            replacement = raw_key[start_index:end_index].upper()
            raw_key = raw_key[0:start_index] + replacement + raw_key[end_index:]
            # raw_key.replace(raw_key[start_index:end_index], replacement)
        else:
            replacement = raw_key[start_index:end_index].lower()
            raw_key = raw_key[0:start_index] + replacement + raw_key[end_index:]
            # raw_key.replace(raw_key[start_index:end_index], replacement)
        print(raw_key)
    elif instruction == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        # to_cut = raw_key[start_index:end_index]
        raw_key = raw_key[:start_index] + raw_key[end_index:]
        print(raw_key)
    command = input().split(">>>")
print(f"Your activation key is: {raw_key}")