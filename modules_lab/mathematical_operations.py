from simple_operations.helper import operation_mapper

data = input().split()

a = float(data[0])
b = float(data[2])
sign = data[1]

print(f'{operation_mapper[sign](a, b):.2f}')
# try:
#     print(f'{operation_mapper[sign](a, b):.2f}')
# except ZeroDivisionError:
#     print("Invalid number b. Should not be ZERO if division.")