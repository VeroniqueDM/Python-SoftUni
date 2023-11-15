employer_one_rate = int(input())
employer_two_rate = int(input())
employer_three_rate = int(input())
total_rate = employer_two_rate + employer_three_rate + employer_one_rate
students = int(input())
hours_counter = 0
while students > 0:
    hours_counter += 1
    students -= total_rate

    if hours_counter % 4 == 0:
        hours_counter +=1




print(f"Time needed: {hours_counter}h.")
