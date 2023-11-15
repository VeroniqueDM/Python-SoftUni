from collections import deque
def math_operations(*args, **kwargs):
    nums = deque(args)
    while nums:
        add_num = nums.popleft()
        kwargs["a"] += add_num
        if nums:
            subtract_num = nums.popleft()
            kwargs["s"] -= subtract_num
        else:
            break
        if nums:
            divide_num = nums.popleft()
            if divide_num != 0:
                kwargs["d"] /= divide_num
        else:
            break
        if nums:
            multiply_num = nums.popleft()
            kwargs["m"] *= multiply_num
        else:
            break
    return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))