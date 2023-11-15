
string_int = [int(x) for x in input().split(", ")]

zero_counter = string_int.count(0)
# print(zero_counter)
first_list = [s for s in string_int if s != 0]
# print(first_list)
second_list = [0] * zero_counter
# print(second_list)
final_list = first_list + second_list
print(final_list)

# for i in range (0, len(string_int)):
#     integer_value = string_int[i]
#     if integer_value == 0:
#         zero_counter +=1
#
# first_list = [s for s in string_int if s != 0]
# second_list = [0] * zero_counter
# final_list = first_list + second_list
# print(first_list)
# print(final_list)