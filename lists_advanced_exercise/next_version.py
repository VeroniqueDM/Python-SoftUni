# current_version = input().split(".")

# current_version_int = [int(x) for x in current_version]
version = [int(s) for s in input().split(".")]
version[-1] += 1

for current_index in range(len(version)-1, -1, -1):
    if version[current_index] > 9:
        version[current_index] = 0
        if current_index-1 >= 0:
            version[current_index-1] += 1
print(".".join(str(s) for s in version))






#
#
# current_version_joined = "".join(current_version)
# current_version_num = int(current_version_joined)
# next_version = current_version_num + 1
# next_version_str = str(next_version)
# print(f"{next_version_str[0]}.{next_version_str[1]}.{next_version_str[2]}")
#
# # print(current_version_num)
#


