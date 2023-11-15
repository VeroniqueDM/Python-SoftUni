deposit=float(input())
deposit_period=int(input())
interest_rate=float(input())/100
total_sum=float(deposit + deposit_period*((deposit*interest_rate)/12))
print(total_sum)