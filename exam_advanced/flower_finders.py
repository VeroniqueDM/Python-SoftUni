from collections import deque

vowels = deque(input().split())
consonants = input().split()
rose = {"r", "o", "s", "e"}
tulip = {"t","u","l","i","p"}
lotus = {"l","o","t","u","s"}
daffodil = {"d","a","f","o","i","l"}
# flowers = ["rose", "daffodil", "tulip", "lotus"]
collected_letters = set()
word_found = False
while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()
    collected_letters.add(vowel)
    collected_letters.add(consonant)

    if rose.issubset(collected_letters):
        word_found = True
        flower = "rose"
        break

    elif tulip.issubset(collected_letters):
        word_found = True
        flower = "tulip"
        break
    elif daffodil.issubset(collected_letters):
        word_found = True
        flower = "daffodil"
        break
    elif lotus.issubset(collected_letters):
        word_found = True
        flower = "lotus"
        break

if word_found:
    print(f"Word found: {flower}")
else:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
