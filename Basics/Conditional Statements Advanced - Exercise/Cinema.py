type = input()
rows = int(input())
columns = int(input())
total_seats = rows*columns
if type == "Premiere":
    total_income = total_seats *12
elif type == "Normal":
    total_income= total_seats * 7.50
elif type == "Discount":
    total_income = total_seats * 5
print(f"{total_income:.2f}")