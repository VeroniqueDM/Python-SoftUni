count = int(input())
total_sum_a = 0
total_sum_b = 0

for i in range (0,count):
    current_num = int(input())
    total_sum_a=total_sum_a+current_num
for i in range (count, count*2):
    current_num = int(input())
    total_sum_b=total_sum_b+current_num
if total_sum_a == total_sum_b:
    print(f"Yes, sum = {total_sum_a}")
else:
    print(f"No, diff = {abs(total_sum_a-total_sum_b)}")


