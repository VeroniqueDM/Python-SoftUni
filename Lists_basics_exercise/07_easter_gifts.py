gifts_list = input().split()

command = input()
while command != "No Money":

    command_list = command.split(" ")
    #print(command_list)
    current_command = command_list[0]
    gift = command_list[1]
    last_index_gift_list = len(gifts_list) - 1


    if current_command == "OutOfStock":
        for element in range(0, len(gifts_list)):
            if gifts_list[element] == gift:
                gifts_list[element] = "None"
    elif current_command == "Required":
        command_index = int(command_list[2])
        if command_index in range(0, last_index_gift_list + 1):
            gifts_list[command_index] = gift
    elif current_command == "JustInCase":

        gifts_list[-1] = command_list[-1]
    command = input()

while "None" in gifts_list:
    gifts_list.remove("None")

join_str = " "
result = join_str.join(gifts_list)
print(result)
