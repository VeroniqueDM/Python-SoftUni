import re
text = input()
regex_emoji = r'(::|\*\*)[A-Z][a-z]{2,}\1'

regex_digits = r'\d'
match_digits = re.findall(regex_digits,text)

coolness_threshold = 1
for digs in match_digits:
    new_digit = int(digs)
    coolness_threshold *=new_digit

match_emojis = re.finditer(regex_emoji,text)


list_emojis = []
for matches in match_emojis:
    new_emoji = matches.group()
    list_emojis.append(new_emoji)
total_emojis = len(list_emojis)
cool_emojis = []
for words in list_emojis:
    ascii_value = 0
    for index in range(2,len(words)-2):
        ascii_value += ord(words[index])
    if ascii_value > coolness_threshold:
        cool_emojis.append(words)
print(f"Cool threshold: {coolness_threshold}")
print(f"{total_emojis} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print(emoji)