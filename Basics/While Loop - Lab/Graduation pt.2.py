name = input()
sum_of_grades = 0
grade_count = 1
fail_count = 0
while grade_count<=12:
    grade_mark = float(input())

    sum_of_grades = sum_of_grades + grade_mark

    if grade_mark < 4:
        fail_count = fail_count + 1
    else:
        grade_count = grade_count + 1
    if fail_count == 2:
        print(f"{name} has been excluded at {grade_count} grade")
        break

if fail_count<2:
    average_grade = sum_of_grades/12
    print(f"{name} graduated. Average grade: {average_grade:.2f}")