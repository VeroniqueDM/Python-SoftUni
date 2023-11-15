import re

some_sentence = input()
valid_urls = []

regex = r'((www.([a-zA-Z0-9]+[\-a-zA-Z0-9]+)*)(\.[a-z]+)+)'
while some_sentence:
    matches = re.finditer(regex,some_sentence)
    if matches:
        for match in matches:
            valid_urls.append(match.group(1))

    some_sentence = input()

for urls in valid_urls:
    print(urls)