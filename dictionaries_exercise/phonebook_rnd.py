new_info = input()
phonebook = {}
while "-" in new_info:
    new_entry = new_info.split("-")
    new_name = new_entry[0]
    new_number = new_entry[1]
    if new_name not in phonebook:
        phonebook[new_name] = 0
    phonebook[new_name] = new_number
    new_info = input()

people_to_check = int(new_info)

for i in range(people_to_check):
    person_to_check = input()
    if person_to_check in phonebook:
        print(f"{person_to_check} -> {phonebook[person_to_check]}")
    else:
        print(f"Contact {person_to_check} does not exist.")

