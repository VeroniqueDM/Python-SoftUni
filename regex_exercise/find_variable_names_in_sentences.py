import re

text= input()

match = re.findall(r"\b_([a-zA-Z0-9]+)\b", text)

print(",".join(match))