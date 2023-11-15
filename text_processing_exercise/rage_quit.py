initial_message = input()
current_str = ""
current_num = ""
new_message = ""
unique_symbols = []
for char in range(0, len(initial_message)):
    if initial_message[char].isdigit() :
        current_num += initial_message[char]
        if char == len(initial_message) - 1:
            new_message += int(current_num) * current_str

        elif not initial_message[char+1].isdigit():
            new_message += int(current_num) * current_str
            current_str = ""
            current_num = ""
    else:
        upper_char = initial_message[char].upper()
        if upper_char not in unique_symbols:
            unique_symbols.append(initial_message[char].upper())

        current_str += initial_message[char].upper()

print(f"Unique symbols used: {len(unique_symbols)}")
print(new_message)
