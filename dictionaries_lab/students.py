command = input().split(":")
students_dict = {}
while len(command) > 1:
    student = command[0]
    current_student_info = {}
    current_student_info["ID"] = command[1]
    current_student_info["course"] = command[2]
    students_dict[student] = current_student_info
    command = input().split(":")

course_list = command[0].split("_")
course = " ".join(course_list)
result_dict = {}
for students in students_dict:
    # for courses in current_student_info:
    if course == students_dict[students]["course"]:
        result_dict[students] = students_dict[students]["ID"]

for k,v in result_dict.items():

    print(f"{k} - {v}")
