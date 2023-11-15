n = int(input())
import re

regex = r'[\|]([A-Z]+)[\|]\:#([A-Za-z]+ [A-Za-z]+)#'

for _ in range(n):
    current_boss = input()
    res = re.findall(regex, current_boss)


    if res:
        print(f"{res[0][0]}, The {res[0][1]}")
        print(f">> Strength: {len(res[0][0])}")
        print(f">> Armor: {len(res[0][1])}")
    else:
        print("Access denied!")