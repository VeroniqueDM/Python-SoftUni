message = input().split()

for a in range (0, len(message)):
    number_as_str = ""
    word = message[a]
    list_of_symbols = list(word)
    for symbol in list_of_symbols:
        is_number = symbol.isdigit()

        if is_number:
            number_as_str += symbol

        else:
            list_of_symbols = [x for x in list_of_symbols if not x.isdigit()]
            character = chr(int(number_as_str))
            list_of_symbols.insert(0, character)
            break

    list_of_symbols[1], list_of_symbols [-1] = list_of_symbols[-1], list_of_symbols[1]
    message[a] = "".join(list_of_symbols)


print(" ".join(message))