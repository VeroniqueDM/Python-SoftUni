n = int(input())
import sys
max_num = -sys.maxsize
sum_numbers = 0
for i in range (1,n+1):
    num = int(input())
    sum_numbers = sum_numbers + num
    if num > max_num:
        max_num = num
sum_numbers = sum_numbers -max_num
if max_num == sum_numbers:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f"Diff = {abs(max_num-sum_numbers)}")