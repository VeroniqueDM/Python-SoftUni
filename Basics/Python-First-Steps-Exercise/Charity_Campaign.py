total_days=int(input())
numberofcooks=int(input())
numberofcakes=int(input())
numberofwafers=int(input())
numberofpancakes=int(input())
total_amount_money=total_days*numberofcooks*(numberofcakes*45+numberofwafers*5.8+numberofpancakes*3.2)
expenses=1/8*total_amount_money
amount_charity=total_amount_money-expenses
print(amount_charity)