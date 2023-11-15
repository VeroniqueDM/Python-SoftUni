n = int(input())
numbers_stack = []
for queries in range(0,n):
    query = input().split()
    command = query[0]
    if command == "2" :
        if len(numbers_stack)>0:
            numbers_stack.pop()
    elif command == "3" :
        if len(numbers_stack) > 0:
            print(max(numbers_stack))
    elif command == "4" :
        if len(numbers_stack) > 0:
            min_n = min(numbers_stack)
            print(min(numbers_stack))
    elif command == "1":
        number_to_add = int(query[1])
        numbers_stack.append(number_to_add)
# reversed_stack = []
# while numbers_stack:
#     reversed_stack.append(str(numbers_stack.pop()))
# print(", ".join(reversed_stack))

while numbers_stack:
    element = numbers_stack.pop()
    if numbers_stack:
        print(element, end= ", ")
    else:
        print(element)