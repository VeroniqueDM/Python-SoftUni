explosions_string = input()
new_string = ""
strength = 0
# index = 0
# while index < len(explosions_string):
for index in range(len(explosions_string)):
    if explosions_string[index] != ">" and strength > 0:
        strength -= 1
    elif explosions_string[index] == ">":
        strength += int(explosions_string[index+1])
        new_string += explosions_string[index]
    else:
        new_string += explosions_string[index]


print(new_string)