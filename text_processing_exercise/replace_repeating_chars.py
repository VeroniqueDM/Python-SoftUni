sequence = input()
new_sequence = sequence[0]

for char in range(1, len(sequence)):
    current_letter = sequence[char]
    previous_letter = sequence[char-1]
    if previous_letter == current_letter:
        pass
    else:
        new_sequence += current_letter

print(new_sequence)