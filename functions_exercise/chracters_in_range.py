
first_character = input()
second_character = input()

def characters_in_range(first, second):
    # collected_symbols = []
    for characters in range (ord(first) + 1, ord(second)):
        character = chr(characters)
        print(character, end=" ")
        # collected_symbols.append(chr(character))
        # return collected_symbols

# result = characters_in_range(first_character, second_character)
# print(' '.join(result))
characters_in_range(first_character, second_character)

print()