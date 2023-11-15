movie = input()
kids_counter = 0
student_counter = 0
standard_counter = 0
total_tickets_counter = 0
while movie != "Finish":
    free_seats = int(input())
    tickets_counter = 0

    for i in range(0, free_seats):
        type_of_ticket = input()

        if type_of_ticket == "End":
            print(f"{movie} - {(tickets_counter / free_seats * 100):.2f}% full.")
            break
        elif type_of_ticket == "kid":
            tickets_counter += 1
            kids_counter += 1
            if free_seats == tickets_counter:
                print(f"{movie} - 100.00% full.")
                break
        elif type_of_ticket == "student":
            tickets_counter += 1
            student_counter += 1
            if free_seats == tickets_counter:
                print(f"{movie} - 100.00% full.")
                break
        elif type_of_ticket == "standard":
            tickets_counter += 1
            standard_counter += 1
            if free_seats == tickets_counter:
                print(f"{movie} - 100.00% full.")
                break
    total_tickets_counter = total_tickets_counter + tickets_counter
    movie = input()
print(f"Total tickets: {total_tickets_counter}")
print(f"{(student_counter/ total_tickets_counter * 100):.2f}% student tickets.")
print(f"{(standard_counter/ total_tickets_counter * 100):.2f}% standard tickets.")
print(f"{(kids_counter/ total_tickets_counter * 100):.2f}% kids tickets.")

