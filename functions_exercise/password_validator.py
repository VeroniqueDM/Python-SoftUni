def is_valid_length(a_password):
    if not 6 <= len(a_password) <= 10:
        print("Password must be between 6 and 10 characters")
        return False
    else:
        return True


def is_char_or_let(a_password):
    if a_password.isalnum():
        return True
    else:
        print("Password must consist only of letters and digits")
        return False

    # for char in a_password:
    #     if not 48<=ord(char)<=57:
    #         if not 65<=ord(char)<=90:
    #             if not 97 <= ord(char) <= 122:
    #                 print("Password must consist only of letters and digits")
    #                 validity = False


def is_two_numbers(a_password):
    a_counter = 0
    for char in a_password:
        if 48 <= ord(char) <= 57:
            a_counter += 1
    if a_counter < 2:
        print("Password must have at least 2 digits")
        return False
    else:
        return True


password = input()
is_valid_list = [is_two_numbers(password), is_valid_length(password), is_char_or_let(password)]
is_valid = all(is_valid_list)
if is_valid == True:
    print("Password is valid")
