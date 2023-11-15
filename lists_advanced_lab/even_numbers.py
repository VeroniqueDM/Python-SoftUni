numbers_string = input().split(", ")

numbers_string_int = [int(n) for n in numbers_string]
# numbers_string_int = list(map(int, numbers_string))
evens_indices = []

# indices = list(filter(lambda i, v: v%2 == 0, enumerate(nums) ))
# indices = list(map(lambda i:i[0] if i[1]%2 == 0, enumerate(nums) ))
#
# #



for nums, v in enumerate(numbers_string_int):
    if v % 2 == 0:
        evens_indices.append(nums)   #(numbers_string_int.index(nums))

print(evens_indices)