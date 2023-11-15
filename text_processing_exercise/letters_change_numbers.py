alphabet = "abcdefghijklmnopqrstuvwxyz"
rdict = dict( [ ( x[1], x[0] ) for x in enumerate(alphabet) ])

for keys, values in rdict.items():
    rdict[keys] +=1

strings_list = [x.strip() for x in input().split()]

total_sum = 0

for string in strings_list:
    first_letter = string[0].isupper()
    last_letter = string[len(string)-1].isupper()
    first_letter_position = rdict[string[0].lower()]
    last_letter_position = rdict[string[len(string) - 1].lower()]
    num_str = ""
    for char in string:
        if char.isdigit():
            num_str += char
    num_int = int(num_str)
    if first_letter:
        current_result = num_int/first_letter_position
    else:
        current_result = num_int*first_letter_position
    if last_letter:
        current_result = current_result - last_letter_position
    else:
        current_result = current_result + last_letter_position
    total_sum += current_result

print(f"{total_sum:.2f}")
