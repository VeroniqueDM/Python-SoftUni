low_grades = int(input())
command_t = input()
grade = int(input())
problem_name = ""
total_problems = 0
fail_count = 0
sum_grades = 0
has_failed = True

while fail_count < low_grades:
    problem_name = command_t
    total_problems = total_problems + 1
    sum_grades = sum_grades + int(grade)
    average = sum_grades / total_problems
    if grade <= 4:
        fail_count = fail_count + 1
        if fail_count == low_grades:
            print(f"You need a break, {low_grades} poor grades.")
            break

    command_t = input()
    if command_t == "Enough":
        has_failed = False
        break
    grade = int(input())


if not has_failed:
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {total_problems}")
    print(f"Last problem: {problem_name}")
