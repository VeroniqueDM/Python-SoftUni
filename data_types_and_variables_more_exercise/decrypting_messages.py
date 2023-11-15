key = int(input())
letters = int(input())
new_word = []
for i in range(letters):
    letter = input()
    new_letter = chr(ord(letter) + key)
    new_word.append(new_letter)

new_word_as_string = "".join(new_word)
print(new_word_as_string)
