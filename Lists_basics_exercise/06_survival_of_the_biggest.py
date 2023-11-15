numbers_list = input().split()
numbers_list_integers = []
numbers_to_remove = int(input())
removed_num_counter = 0
for numbers in range(len(numbers_list)):
    numbers_list_integers.append(int(numbers_list[numbers]))



while removed_num_counter < numbers_to_remove:
    numbers_list_integers.remove(min(numbers_list_integers))
    removed_num_counter +=1

print(*numbers_list_integers, sep=", ")


