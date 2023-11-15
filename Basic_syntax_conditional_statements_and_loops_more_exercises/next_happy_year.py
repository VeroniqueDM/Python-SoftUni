current_year_list = list(input())

current_year_unique = list(set(current_year_list))
current_year_str = "".join(current_year_list)
current_year_int = int(current_year_str)


while len(current_year_list) != len(current_year_unique):
    current_year_int += 1
    current_year_str = str(current_year_int)
    current_year_list = list(current_year_str)
    current_year_unique = list(set(current_year_list))

print(current_year_int)

# current_year_list = list(input())
# current_year_str = "".join(current_year_list)
# current_year_int = int(current_year_str)
#
#
# for symbols in current_year_list:
#
#
#
#
# def is_happy(a,b,c,d):
#     if a!=b and a!=c and a!=d and b!=c  and b != d and c != d:
#         return True
#
# while is_happy(current_year_list[0],current_year_list[1], current_year_list[2], current_year_list[3]) != True:
#     current_year_int +=1
#     current_year_str = str(current_year_int)
#     current_year_list = list(current_year_str)
#
# print(current_year_int)