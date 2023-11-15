def is_palindrome(number:str):

    reverse_number = number[::-1]

    if reverse_number == number:
        return True
    else:
        return False



numbers = input().split(", ")
# numbers_integers = []
# for num in numbers:
#     numbers_integers.append(int(num))

for nums in numbers:
    print(is_palindrome(nums))