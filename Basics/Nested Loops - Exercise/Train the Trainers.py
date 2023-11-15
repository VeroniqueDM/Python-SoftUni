n = int(input())
command = input()
pres_count = 0
total_sum_grades = 0
while command != "Finish":
    current_presentation = command
    pres_count +=1
    current_sum_grades = 0

    for i in range (1, n + 1):
        grade = float(input())
        current_sum_grades += grade
    print( f"{current_presentation} - {(current_sum_grades/n):.2f}.")
    total_sum_grades += current_sum_grades/n
    command = input()
print(f"Student's final assessment is {(total_sum_grades/pres_count):.2f}." )