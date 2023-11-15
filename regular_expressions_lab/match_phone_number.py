import re

text = input()
#
# regex = r"\+359( |-)2(\1)\d{3}(\1)\d{4}\b"
res = ""
matches = re.finditer(r"\+359( |-)2(\1)\d{3}(\1)\d{4}\b",text)
for match in matches:
    match_str = match.group(0)
    res += match_str + ", "

print(res.rstrip(", "))