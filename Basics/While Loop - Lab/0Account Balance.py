deposit = input()
total = 0

while deposit != "NoMoreMoney":
    if float(deposit) < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {(float(deposit)):.2f}")
        total = total+float(deposit)
        deposit = input()
print (f"Total: {total:.2f}")