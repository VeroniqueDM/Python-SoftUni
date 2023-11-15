words = input().split()
dictionary_n = {}

for word in words:
    word_lower = word.lower()
    if word_lower not in dictionary_n:
        dictionary_n[word_lower] = 0
    dictionary_n[word_lower] +=1
dictionary_odd = []
for current_word in dictionary_n:
    if dictionary_n[current_word] % 2 == 1:
       dictionary_odd.append(current_word)

result = " ".join(dictionary_odd)
print(result)
