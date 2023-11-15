

def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    res = []
    for func_ref, func_params in args:
        res.append(func_ref(*func_params))
    return res




    # for a in args:
    #     b = a[0](a[1][0], a[1][1])
    #     res.append(b)
    # return res
    #

print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
