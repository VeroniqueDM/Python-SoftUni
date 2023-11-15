countries = input().split(", ")
capitals = input().split(", ")

countries_and_capitals = {countries[i]:capitals[i] for i in range (0, len(countries))}

for a in countries_and_capitals:
    print(f"{a} -> {countries_and_capitals[a]}")