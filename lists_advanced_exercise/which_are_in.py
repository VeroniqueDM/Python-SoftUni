string_one = input().split(", ")
string_two = input().split(", ")

result = []

for word in string_one:
    for words in string_two:
        if word in words and not word in result:
            result.append(word)

print(result)