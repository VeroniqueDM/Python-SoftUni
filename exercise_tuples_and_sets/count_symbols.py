text_string = input()
char_list = {}
for char in text_string:
    if char not in char_list:
        char_list[char] = 1
    else:
        char_list[char] += 1

for key, value in sorted(char_list.items()):
    print(f'{key}: {value} time/s')