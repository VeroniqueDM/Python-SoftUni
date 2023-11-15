
numbers = [int(x) for x in input().split(", ")]

counter = 0
group_of_numbers = 10
while counter < len(numbers):
    collected_nums = []
    for number in numbers:
        if group_of_numbers - 10 < number <= group_of_numbers:
            collected_nums.append(number)

            counter += 1

    print(f"Group of {group_of_numbers}'s: {collected_nums}")
    group_of_numbers += 10



