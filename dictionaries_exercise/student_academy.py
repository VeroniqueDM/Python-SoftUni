total_grades = int(input())
students_dict = {}
for a in range(total_grades):
    student = input()
    grade = float(input())

    if student not in students_dict:
        students_dict[student] = []
    students_dict[student].append(grade)

above_average = {}
for k,v in students_dict.items():
    average = sum(v)/len(v)
    if average >= 4.50:
        above_average[k] = average

sorted_above_average = dict(sorted(above_average.items(), key=lambda kvpt:kvpt[1], reverse=True))

for a,b in sorted_above_average.items():
    print(f"{a} -> {b:.2f}")