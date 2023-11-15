string = list(input())
capital_indices = []
indices_counter = 0
for index in string:
    if index.isupper() == True:
        capital_indices.append(indices_counter)
    indices_counter += 1

print(capital_indices)

