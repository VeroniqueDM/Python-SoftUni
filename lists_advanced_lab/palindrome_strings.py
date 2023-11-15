list_of_words = input().split()
palindrome = input()
palindromes_list = []
palindrome_counter = 0
for words in list_of_words:
    reversed_word = words[::-1]
    if reversed_word == words:
        palindromes_list.append(words)
    if words == palindrome:
        palindrome_counter += 1


print(palindromes_list)
print(f"Found palindrome {palindrome_counter} times")
