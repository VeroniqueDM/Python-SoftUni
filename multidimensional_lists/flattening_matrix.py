
rows = int(input())
result = []
for _ in range(rows):
    nums = [int(x) for x in input().split(", ")]
    result.extend(nums)







# rows = int(input())
#
# matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
# flat_matrix = []
#
# for a in range(rows):
#     for v in matrix[a]:
#         flat_matrix.append(v)
#
# print(flat_matrix)