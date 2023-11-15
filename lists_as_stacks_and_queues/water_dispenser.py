from collections import deque

liters = int(input())
line = deque()
name = input()
while not name == "Start":
    line.append(name)

    name = input()

command = input()

while not command == "End":
    if command.isdigit():
        required_liters = int(command)
        name = line.popleft()
        if liters >= required_liters:
            liters -= required_liters
            print(f"{name} got water")
        else:
            print(f"{name} must wait")

    else:
        refill_command = command.split()
        refill_liters = int(refill_command[1])
        liters += refill_liters
    command = input()


print(f"{liters} liters left")