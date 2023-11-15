movie = input()
total_tickets_counter = 0
kids_counter = 0
student_counter = 0
standard_counter = 0
total_kids_counter = 0
total_student_counter = 0
total_standard_counter = 0

while movie != "Finish":
    free_seats = int(input())
    tickets_counter = 0

    while free_seats > tickets_counter:
        type_of_ticket = input()
        kids_counter = 0
        student_counter = 0
        standard_counter = 0
        if type_of_ticket == "End":
            print(f"{movie} - {tickets_counter / free_seats * 100}% full. ")
            break
        elif type_of_ticket == "kid":
            tickets_counter += 1
            kids_counter += 1
            if free_seats == tickets_counter:
                print(f"{movie} - 100% full.")
                break
        elif type_of_ticket == "student":
            tickets_counter += 1
            student_counter += 1
            if free_seats == tickets_counter:
                print(f"{movie} - 100% full.")
                break
        elif type_of_ticket == "standard":
            tickets_counter += 1
            standard_counter += 1
            if free_seats == tickets_counter:
                print(f"{movie} - 100% full.")
                break
    total_kids_counter += kids_counter
    total_student_counter += student_counter
    total_standard_counter += standard_counter
    total_tickets_counter = total_tickets_counter + tickets_counter
    movie = input()
print(f"Total tickets: {total_tickets_counter}")
print(f"{total_student_counter / total_tickets_counter * 100}% student tickets.")
print(f"{total_standard_counter / total_tickets_counter * 100}% standard tickets.")
print(f"{total_kids_counter / total_tickets_counter * 100}% kids tickets.")
