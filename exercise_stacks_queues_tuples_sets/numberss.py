first_sequence = set([int(x) for x in input().split()])
second_sequence = set([int(x) for x in input().split()])

n = int(input())

for _ in range(n):
    command = input().split()

    if command[0] == "Add":
#        add_sequence = set([int(x) for x in command[2:]])
        if command[1] == "First":
            [first_sequence.add(int(x)) for x in command[2:]]
            # first_sequence.union(add_sequence)
        else:
            [second_sequence.add(int(x)) for x in command[2:]]
           # second_sequence.union(add_sequence)
    elif command[0] == "Remove":
        #remove_sequence = set([int(x) for x in command[2:]])
        if command[1] == "First":
            [first_sequence.discard(int(x)) for x in command[2:]]
        else:
            [second_sequence.discard(int(x)) for x in command[2:]]
    else:
        if first_sequence < second_sequence or second_sequence < first_sequence:
            print(True)
        else:
            print(False)

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")