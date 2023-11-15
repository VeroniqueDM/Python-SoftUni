numbers = input().split()
message = list(input())
list_indices = []

for number in numbers:
    current_list = [int(x) for x in number]
    index = sum(current_list)
    list_indices.append(index)


list_letters = []

for ind in list_indices:
    if ind < len(message):
        list_letters.append(message[ind])
        del message[ind]
    else:
        new_pos = ind-(len(message))
        list_letters.append(message[new_pos])
        del message[new_pos]

print("".join(list_letters))



