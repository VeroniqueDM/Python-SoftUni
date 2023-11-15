import re

text = input()

regex = r'((?<=\s)([a-z0-9]+[-\.\_a-z0-9]*)@([a-z]+)(-[a-z-]+)*\.([a-z\.]+))\b'

matches = re.findall(regex,text)

for match in matches:
    print(match[0].rstrip('.'))
    # print(f"{match[0]}@{match[1]}.{match[3].)}")