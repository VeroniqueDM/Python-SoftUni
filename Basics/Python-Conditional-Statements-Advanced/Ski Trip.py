days_count = int(input())
days_count = days_count - 1
type_of_room = input()
review = input()
discount = 0
price = 0
total_price = 0
if type_of_room == "room for one person":
    price = days_count * 18
elif type_of_room == "apartment":
    price = days_count * 25
    if days_count<10:
        discount = price*0.3
    elif 15>=days_count>=10:
        discount = price*0.35
    elif days_count>15:
        discount = price*0.5
elif type_of_room == "president apartment":
    price = days_count * 35
    if days_count<10:
        discount = price*0.1
    elif 15>=days_count>=10:
        discount = price*0.15
    elif days_count>15:
        discount = price*0.2
discount_price = price-discount
if review == "positive":
    total_price = discount_price + discount_price*0.25
elif review == "negative":
    total_price = discount_price - discount_price*0.1
print(f"{total_price:.2f}")