import re

text = input()


match = re.finditer(r"(^|(?<=\s))-?\d+(\.\d+)?(?=\s|$)",text)

valid_nums = []

for nums in match:
    new_match = nums.group(0)
    if new_match not in valid_nums:
        valid_nums.append(new_match)

print(" ".join(valid_nums))