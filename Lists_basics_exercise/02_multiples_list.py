factor = int(input())
count = int(input())
list_multiples = []

for i in range (1, count + 1):
    result = i * factor
    list_multiples.append(result)

print(list_multiples)