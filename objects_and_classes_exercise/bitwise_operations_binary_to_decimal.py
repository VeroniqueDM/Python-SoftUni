first_number = int(input())
looked_num = int(input())
counter = 0
while first_number != 0:
    remainder = first_number % 2
    if remainder == looked_num:
        counter +=1
    first_number = first_number // 2

print(counter)