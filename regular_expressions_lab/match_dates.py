import re

text = input()

matches = re.findall(r"(\d{2})(\.|-|\/)([A-Z][a-z]{2})(\2)(\d{4})", text)

for match in matches:
    day = match[0]
    month = match[2]
    year = match[4]
    print(f"Day: {day}, Month: {month}, Year: {year}")