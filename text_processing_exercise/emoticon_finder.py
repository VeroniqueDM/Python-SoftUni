input_text = input()

emoticons = []

for a in range (0, len(input_text)):
    char = input_text[a]
    if char == ":":

        new_emoticon = char + input_text[a + 1]
        emoticons.append(new_emoticon)

[print(x) for x in emoticons]