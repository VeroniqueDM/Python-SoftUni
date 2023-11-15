#
# def multiply_string(text, count):
#     return text * count
#
# # res = multiply_string("")

text = input()
count = int(input())

x = lambda t, c: t * c

res_lambda = x(text, count)

print(res_lambda)