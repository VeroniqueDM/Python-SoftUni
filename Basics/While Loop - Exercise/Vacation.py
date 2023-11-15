excursion_price = float(input())
current_savings = float(input())
activity = input()
amount = float(input())
days_counter = 0
spending_counter = 0
while current_savings < excursion_price:
    days_counter = days_counter + 1
    if activity == "spend":
        current_savings = current_savings - amount
        if current_savings < 0:
            current_savings = 0
        spending_counter = spending_counter + 1
        if spending_counter == 5:
            print("You can't save the money.")
            print(f"{days_counter}")
            break
    elif activity == "save":
        current_savings = current_savings + amount
        spending_counter = 0
        if current_savings >= excursion_price:
            print(f"You saved the money for {days_counter} days.")
            break
    activity = input()
    amount = float(input())

