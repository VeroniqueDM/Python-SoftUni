number_of_lines = int(input())

mix_string = []

for i in range (0, number_of_lines):
    line = input()
    mix_string.append(line)

brackets_string = [x for x in mix_string if x == ")" or x == "("]
is_balanced = True
for brackets in range (0, len(brackets_string)-1):
    if brackets_string[brackets] == brackets_string[brackets+1]:
        is_balanced = False

    else:
        continue
if brackets_string[0] != "(" or brackets_string[-1] != ")":
    is_balanced = False

if brackets_string == None:
    is_balanced = True

if is_balanced == False:
    print("UNBALANCED")
else:
    print("BALANCED")
