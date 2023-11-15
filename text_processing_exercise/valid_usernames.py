usernames = input().split(", ")
valid_usernames =[]
for uname in usernames:
    is_valid = True
    if 3<= len(uname) <= 16:

        for char in uname:
            if char.isdigit() or char.isalpha() or char == "-" or char == "_":
                pass
            else:
                is_valid = False
                break
    else:
        is_valid = False
    if is_valid == True:
        valid_usernames.append(uname)

for username in valid_usernames:
    print(username)