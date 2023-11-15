characters = input().split(", ")
ascii_values = {x:ord(x) for x in characters}

# for i in characters:
#     ascii_values[i] = ord(i)

print(ascii_values)