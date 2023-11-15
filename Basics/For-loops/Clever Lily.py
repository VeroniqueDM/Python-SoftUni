lily_age = int(input())
washingm_price = float(input())
toy_price = int(input())
number_of_toys =0
moneygift = 0
moneygift_total = moneygift
for i in range (1,lily_age+1):
    if i%2 == 0:
        moneygift = moneygift + 10
        moneygift_total = moneygift_total + moneygift - 1
    else:
        number_of_toys = number_of_toys + 1
        total_toy_price = number_of_toys * toy_price
money_total = total_toy_price + moneygift_total
if money_total>=washingm_price:
    print(f"Yes! {(money_total-washingm_price):.2f}")
else:
    print(f"No! {abs(money_total-washingm_price):.2f}")