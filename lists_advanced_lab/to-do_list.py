notes = [0] * 11

command = input()
while command != "End":
    command_list = command.split("-")
    priority = int(command_list[0])
    note = command_list[1]

    notes.pop(priority)
    notes.insert(priority, note)

    command = input()

while 0 in notes:
    notes.remove(0)

print(notes)