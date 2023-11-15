list_of_people = input().split()
k = int(input())
current_index = 0
list_executed = []

while list_of_people:
    current_index += (k-1)
    if current_index < len(list_of_people):
        list_executed.append(list_of_people[current_index])
        del list_of_people[current_index]
    else:
        while current_index >= len(list_of_people):
            current_index = current_index - len(list_of_people)
        list_executed.append(list_of_people[current_index])
        del list_of_people[current_index]


result = ",".join(list_executed)

print(f"[{result}]")

