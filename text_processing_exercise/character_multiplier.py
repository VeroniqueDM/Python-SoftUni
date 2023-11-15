string_pair = input().split()
first_word = string_pair[0]
second_word = string_pair[1]
difference = abs(len(first_word) - len(second_word))
total_sum = 0

if len(first_word) > len(second_word):
    for index in range (0,len(second_word)):
        total_sum += ord(first_word[index]) * ord(second_word[index])
    for a in range(len(first_word)-difference, len(first_word)):
        total_sum += ord(first_word[a])
elif len(first_word) <len(second_word):
    for index in range(0, len(first_word)):
        total_sum += ord(first_word[index]) * ord(second_word[index])
    for a in range(len(second_word) - difference, len(second_word)):
        total_sum += ord(second_word[a])
else:
    for index in range(0, len(first_word)):
        total_sum += ord(first_word[index]) * ord(second_word[index])

print(total_sum)