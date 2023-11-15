# n = int(input())
# comb_count = 0
#
# for x1 in range (0, n+1):
#     for x2 in range (0,n+1):
#         for x3 in range (0, n+1):
#             if x1+x2+x3 == n:
#                 comb_count += 1
#
# print(comb_count)


n = int(input())
comb_count = 0
other_count = 0
for x1 in range (0, n+1):
    for x2 in range (0,n+1):
        for x3 in range (0, n+1):
            if x1+x2+x3 == n:
                comb_count += 1
            else:
               other_count += 1
print(comb_count)
print(f"{comb_count+other_count}")

