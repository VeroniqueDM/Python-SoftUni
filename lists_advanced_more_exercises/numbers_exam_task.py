numbers_str = input().split()
numbers_int = [int(x) for x in numbers_str]

command = input().split()

while command[0] != "Finish":
    if command[0] == "Add":
        numbers_int.append(command[1])
    elif command[0] == "Remove":
        numbers_int.remove(command[1])
    elif command[0] == "Replace":
        if int(command[1]) in numbers_int:
            index = numbers_int.index(int(command[1]))
            numbers_int[index] = int(command[2])
    elif command[0] == "Collapse":
        numbers_int = [x for x in numbers_str if x>= int(command[1])]

print(numbers_int)
