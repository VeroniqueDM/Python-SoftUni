import re
text = input()

regex = r'(@|#)([a-zA-Z]{3,})(\1){2}([a-zA-Z]{3,})(\1)'

matches = re.findall(regex,text)
pairs_list = []
for pairs in matches:
    first_word = pairs[1]
    second_word = pairs[3]
    second_word_reversed = second_word[::-1]
    if first_word == second_word_reversed:
        new_match = first_word + " <=> " + second_word
        pairs_list.append(new_match)

if matches:
    print(f"{len(matches)} word pairs found!")
else:
    print("No word pairs found!")
if pairs_list:
    print("The mirror words are:")
    print(", ".join(pairs_list))
else:
    print("No mirror words!")
