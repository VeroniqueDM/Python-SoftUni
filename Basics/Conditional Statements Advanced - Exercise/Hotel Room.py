month = input()
number_of_days = int(input())
studio_price = 0
apartment_price = 0
type_of_room = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if 14>=number_of_days > 7:
        studio_price = studio_price*0.95
    elif number_of_days>14:
        studio_price = studio_price*0.7
elif month == "June" or month == "September":
    studio_price = 75.2
    apartment_price = 68.70
    if number_of_days > 14:
        studio_price = studio_price *0.8
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
if number_of_days>14:
    apartment_price = apartment_price*0.90
total_price_studio = studio_price*number_of_days
total_price_apartment = apartment_price * number_of_days
print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")