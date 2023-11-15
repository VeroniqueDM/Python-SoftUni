# text = input().split()
# even_len_list = [s for s in text if len(s) % 2 == 0]
# # res = "".join(even_len_list)
# for r in even_len_list:
#     print(r)
#



print('\n'.join(s for s in input().split() if len(s)%2 == 0))