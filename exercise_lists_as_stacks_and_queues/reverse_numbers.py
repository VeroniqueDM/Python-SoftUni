nums_string = [int(x) for x in input().split()]

for nums in nums_string[::-1]:
    print(nums_string.pop(), end=" ")