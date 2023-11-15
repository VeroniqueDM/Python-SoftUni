command = input()
number_of_adults = 0
number_of_children = 0
toys_total = 0
sweaters_total = 0
while command != "Christmas":

    age = int(command)
    if age <= 16:
        number_of_children += 1
        toys_total += 1
    else:
        number_of_adults +=1
        sweaters_total +=1
    command = input()

money_for_toys = number_of_children *5
money_for_sweaters = number_of_adults * 15

print(f"Number of adults: {number_of_adults}")
print(f"Number of kids: {number_of_children}")
print(f"Money for toys: {money_for_toys}")
print(f"Money for sweaters: {money_for_sweaters}")