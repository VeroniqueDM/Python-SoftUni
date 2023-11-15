nums = [int(x) for x in input().split()]

for ind in range(len(nums)):
    min_num = nums[ind]
    min_ind = ind
    for next_ind in range(ind+1, len(nums)):
        next_num = nums[next_ind]
        if next_num< min_num:
            min_num = next_num
            min_ind = next_ind
    nums[ind], nums[min_ind] = nums[min_ind], nums[ind]

# print(' '.join([str(i) for i in nums]))
print(*nums, sep=' ')