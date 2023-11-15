employees_happiness = input().split()
employees_happiness_int = [int(n) for n in employees_happiness]
factor = int(input())
employees_happiness_int_multiplied = [x*factor for x in employees_happiness_int]
# employees_happiness_int_multiplied = list(map(lambda x: int(x) * factor, employees_happiness_int))
total_happiness_average = sum(employees_happiness_int_multiplied)/len(employees_happiness)
filtered_above_average = list(filter(lambda x: x>= total_happiness_average, employees_happiness_int_multiplied))


if len(filtered_above_average) >= len(employees_happiness)/2:
    print(f"Score: {len(filtered_above_average)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_above_average)}/{len(employees_happiness)}. Employees are not happy!")