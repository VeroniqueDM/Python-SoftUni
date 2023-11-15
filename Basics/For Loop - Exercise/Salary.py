n = int(input())
salary = float(input())
fine_amount = 0
for i in range(1, n + 1):
    website = input()
    if website == "Facebook":
        fine_amount = fine_amount + 150
    elif website == "Instagram":
        fine_amount = fine_amount + 100
    elif website == "Reddit":
        fine_amount = fine_amount + 50
    if fine_amount >= salary:
        print("You have lost your salary.")
        break

if salary > fine_amount:
    print(f"{salary - fine_amount:.0f}")
