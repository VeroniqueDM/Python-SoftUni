command = input()
numbers = [int(x) for x in input().split()]

parity = 0 if command == "Even" else 1
res = sum([x for x in numbers if x%2 == parity]) * len(numbers)
print(res)

#
# if command == "Odd":
#     odd_nums = sum([x for x in numbers if x%2 !=0])
#     res = odd_nums * len(numbers)
#     print(res)
# else:
#     even_nums = sum([x for x in numbers if x%2 ==0])
#     res = even_nums * len(numbers)
#     print(res)
