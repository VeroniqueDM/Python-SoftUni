import re

text=input()
final_list = []
while True:
    if text:
        matches = re.findall(r"\d+", text)
        for match in matches:
            final_list.append(match)
        text = input()
    else:
        break

print(" ".join(final_list))