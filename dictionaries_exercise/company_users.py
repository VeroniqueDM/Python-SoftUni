command = input()

companies_and_employers = {}

while "->" in command:
    new_entry = command.split(" ->")
    company_name = new_entry[0]
    employee_id = new_entry[1]
    if company_name not in companies_and_employers:
        companies_and_employers[company_name] = []
    if employee_id not in companies_and_employers[company_name]:
        companies_and_employers[company_name].append(employee_id)

    command = input()

sorted_dict = dict(sorted(companies_and_employers.items(), key=lambda kv:kv[0]))

for a,b in sorted_dict.items():
    print(a)
    for b in sorted_dict[a]:
        print(f"--{b}")