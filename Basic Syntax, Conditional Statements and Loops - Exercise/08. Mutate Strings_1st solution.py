text_1 = input()
text_2 = input()
first_string = text_1
last_string = ""
for c in range (0, len(text_2)):
    for e in range (c+1):
        last_string += text_2[e]
    for z in range (c+1, len(text_2)):
       last_string += text_1[z]
    if last_string != first_string:
        print(last_string)
        first_string = last_string
    last_string = ""