command = input()
courses_collection = {}

while ":" in command:
    new_entry = command.split(" :")
    course = new_entry[0]
    student_name = new_entry[1]
    if course not in courses_collection:
        courses_collection[course] = []
    courses_collection[course].append(student_name)
    courses_collection[course].sort()

    command = input()
sorted_courses = dict(sorted(courses_collection.items(), key=lambda k:len(k[1]), reverse=True))

for k,v in sorted_courses.items():
    registered_students = len(sorted_courses[k])

    print(f"{k}: {registered_students}")
    for v in courses_collection[k]:
        print(f"--{v}")
