command = input()
results = {}
submissions = {}
while command != "exam finished":
    submission = command.split("-")
    username = submission[0]
    if submission[1] == "banned":
        del results[username]
    else:
        language = submission[1]
        points = int (submission[2])
        if username not in results:
            results[username] = 0
        if results[username] < points:
            results[username] = points
        if language not in submissions:
            submissions[language] = 0
        submissions[language] +=1

    command = input()

results_sorted = sorted(results.items(), key=lambda kvpt: (-kvpt[1], kvpt[0]))
submissions_sorted = sorted(submissions.items(), key=lambda kvp: (-kvp[1], kvp[0]))

print("Results:")
for v in results_sorted:
    student = v[0]
    points = v[1]
    print(f"{student} | {points}")
print("Submissions:")
for a in submissions_sorted:
    course = a[0]
    subs = a[1]
    print(f"{course} - {subs}")