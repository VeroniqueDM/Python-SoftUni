text = input()
vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
new_text_list = [c for c in text if c not in vowels]

new_text = "".join(new_text_list)

print(new_text)