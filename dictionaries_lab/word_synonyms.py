number_of_words = int(input())

synonyms_dict = {}
for i in range (0, number_of_words):
    word = input()
    synonym = input()
    if word not in synonyms_dict:
        synonyms_dict[word] = []
    synonyms_dict[word].append(synonym)

for words,synonyms in synonyms_dict.items():
    synonym_list = ", ".join(synonyms)
    print(f"{words} - {synonym_list}")
