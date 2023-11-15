words = input().split()

size = [0]* len(words)
size[0]=1
prev = [None] * len(words)

best_index = 0
best_size = 1

for index in range(1, len(words)):
    current_word = words[index]
    current_best_size = 1
    current_parent = None
    for prev_index in range(index - 1, -1, -1):
        prev_word = words[prev_index]
        if len(prev_word)>=len(current_word):
            continue
        if size[prev_index] +1 >= current_best_size:
            current_best_size = size[prev_index] + 1
            current_parent = prev_index
    size[index] = current_best_size
    prev[index] = current_parent
    if current_best_size>best_size:
        best_size = current_best_size
        best_index = index

# print(best_size)
result = []

while best_index is not None:
    result.append(words[best_index])
    best_index = prev[best_index]

print(*list(reversed(result)), sep=' ')