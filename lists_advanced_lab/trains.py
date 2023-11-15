number = int(input())

train_wagons_list = [0 for num in range(number)]
command = input()

while command != "End":
    command_list = command.split()
    if command_list[0] == "add":
        train_wagons_list[number-1] += int(command_list[1])
    elif command_list[0] == "insert":
        train_wagons_list[int(command_list[1])] += int(command_list[2])
    elif command_list[0] == "leave":
        train_wagons_list[int(command_list[1])] -= int(command_list[2])
    command = input()


print(train_wagons_list)