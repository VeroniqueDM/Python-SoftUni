def merge_arrays(left, right):
    result = [None] * (len(left) + len(right))
    left_ind = 0
    right_ind = 0
    result_ind = 0
    while left_ind < len(left) and right_ind < len(right):
        if left[left_ind] < right[right_ind]:
            result[result_ind] = left[left_ind]
            left_ind += 1
        else:
            result[result_ind] = right[right_ind]
            right_ind += 1
        result_ind += 1
    while left_ind < len(left):
        result[result_ind] = left[left_ind]
        left_ind += 1
        result_ind += 1
    while right_ind < len(right):
        result[result_ind] = right[right_ind]
        right_ind += 1
        result_ind += 1
    return result


def merge_sort(nums):
    if len(nums) == 1:
        return nums
    mid_ind = len(nums) // 2
    left = nums[:mid_ind]
    right = nums[mid_ind:]
    return merge_arrays(merge_sort(left), merge_sort(right))


nums = [int(x) for x in input().split()]
print(*merge_sort(nums), sep=' ')
