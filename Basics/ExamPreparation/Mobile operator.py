contract_length = input()
type_of_contract = input()
internet = input()
months_payment = int(input())
monthly_base_fee = 0
internet_fee = 0

if contract_length == "one":
    if type_of_contract == "Small":
        monthly_base_fee = 9.98

    elif type_of_contract == "Middle":
        monthly_base_fee = 18.99
    elif type_of_contract == "Large":
        monthly_base_fee = 25.98
    elif type_of_contract == "ExtraLarge":
        monthly_base_fee = 35.99

elif contract_length == "two":
    if type_of_contract == "Small":
        monthly_base_fee = 8.58

    elif type_of_contract == "Middle":
        monthly_base_fee = 17.09
    elif type_of_contract == "Large":
        monthly_base_fee = 23.59
    elif type_of_contract == "ExtraLarge":
        monthly_base_fee = 31.79

if internet == "yes":
    if monthly_base_fee <= 10:
        internet_fee = 5.50
    elif 10<monthly_base_fee<=30:
        internet_fee = 4.35
    elif monthly_base_fee>30:
        internet_fee = 3.85

base_plus_internet = (monthly_base_fee + internet_fee)*months_payment
if contract_length == "two":
    base_plus_internet = base_plus_internet - base_plus_internet*0.0375

print(f"{base_plus_internet:.2f} lv.")
