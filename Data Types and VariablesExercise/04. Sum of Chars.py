number_of_characters = int(input())
total_sum = 0

for chars in range (1, number_of_characters+1):
    character = input()
    value = ord(character)
    total_sum += value

print(f"The sum equals: {total_sum}")