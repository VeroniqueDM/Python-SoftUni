word = input()

characters_list = []

for i,v in enumerate(word):
    if v != " ":
        characters_list.append(v)

characters_dict = {}

for a in characters_list:
    if a not in characters_dict:
        characters_dict[a] = 0
    characters_dict[a] += 1

for chars in characters_dict:
    print(f"{chars} -> {characters_dict[chars]}")