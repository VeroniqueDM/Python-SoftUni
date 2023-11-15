count = int(input())
total_sum_a = 0
total_sum_b = 0

for i in range (1,count+1):
    current_num = int(input())
    if i%2 == 0:
        total_sum_a=total_sum_a+current_num
    else:
        total_sum_b=total_sum_b+current_num

if total_sum_a == total_sum_b:
    print("Yes")
    print(f"Sum = {total_sum_a}")
else:
    print("No")
    print(f"Diff = {abs(total_sum_a-total_sum_b)}")


