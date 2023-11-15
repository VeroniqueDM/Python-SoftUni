text = input().lower()

counter = 0
word_one = "sand"
word_two = "fish"
word_three = "water"
word_four = "sun"

if word_one in text:
   res = text.count(word_one)
   counter +=res
if word_two in text:
    res = text.count(word_two)
    counter += res
if word_three in text:
    res = text.count(word_three)
    counter += res
if word_four in text:
    res = text.count(word_four)
    counter += res

print(counter)


