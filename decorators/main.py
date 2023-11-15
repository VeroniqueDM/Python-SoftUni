# # # def hello_function():
# # #     def say_hi():
# # #         return "Hi"
# # #     return say_hi
# # # hello = hello_function()
# # # hello()
# #
# #
# # def uppercase(function):
# #     def wrapper():
# #         result = function()
# #         uppercase_result = result.upper()
# #         return uppercase_result
# #
# #     return wrapper
# #
# # def say_hi():
# #     return 'hello there'
# #
# # decorate = uppercase(say_hi)
# # print(decorate())
#
# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator
#
#
# @repeat(4)
# def say_hi():
#     print("Hello")
# ----------------------------------

from time import time, sleep

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(end - start)
        return result
    return wrapper

@measure_time
def double_array(nums):
    sleep(4)
    return nums + nums

print(double_array([1,2,3]))